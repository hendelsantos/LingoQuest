"use client";

import { type FormEvent, useEffect, useState } from "react";

import { ApiError, apiGet, apiPatch, apiPost, type AuthUser } from "@/lib/auth";
import { getCourses, type CourseSummary, type Enrollment, type EnrollmentStatus } from "@/lib/learning";

export function EnrollmentManager() {
  const [students, setStudents] = useState<AuthUser[]>([]);
  const [courses, setCourses] = useState<CourseSummary[]>([]);
  const [enrollments, setEnrollments] = useState<Enrollment[]>([]);
  const [studentId, setStudentId] = useState("");
  const [courseSlug, setCourseSlug] = useState("");
  const [loading, setLoading] = useState(true);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [message, setMessage] = useState("");

  useEffect(() => {
    const controller = new AbortController();
    Promise.all([
      apiGet<AuthUser[]>("/api/v1/admin/users/?role=STUDENT&active=true", controller.signal),
      getCourses(controller.signal),
      apiGet<Enrollment[]>("/api/v1/admin/enrollments/", controller.signal),
    ]).then(([availableStudents, availableCourses, currentEnrollments]) => {
      setStudents(availableStudents);
      setCourses(availableCourses);
      setEnrollments(currentEnrollments);
      setStudentId(availableStudents[0]?.id ?? "");
      setCourseSlug(availableCourses[0]?.slug ?? "");
    }).catch((reason: unknown) => {
      if (!controller.signal.aborted) {
        setError(reason instanceof ApiError ? reason.message : "Não foi possível carregar as matrículas.");
      }
    }).finally(() => {
      if (!controller.signal.aborted) setLoading(false);
    });
    return () => controller.abort();
  }, []);

  async function createEnrollment(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setBusy(true);
    setError("");
    setMessage("");
    try {
      const enrollment = await apiPost<Enrollment>("/api/v1/admin/enrollments/", {
        studentId,
        courseSlug,
      });
      setEnrollments((current) => [enrollment, ...current]);
      setMessage(`Matrícula de ${enrollment.student.name} criada com sucesso.`);
    } catch (reason) {
      setError(reason instanceof ApiError ? reason.message : "Não foi possível criar a matrícula.");
    } finally {
      setBusy(false);
    }
  }

  async function changeStatus(enrollment: Enrollment, status: EnrollmentStatus) {
    setError("");
    setMessage("");
    try {
      const updated = await apiPatch<Enrollment>(
        `/api/v1/admin/enrollments/${enrollment.id}/`,
        { status },
      );
      setEnrollments((current) => current.map((item) => item.id === updated.id ? updated : item));
      setMessage(`Status de ${updated.student.name} atualizado.`);
    } catch (reason) {
      setError(reason instanceof ApiError ? reason.message : "Não foi possível atualizar a matrícula.");
    }
  }

  if (loading) return <div className="lesson-skeleton">Carregando gestão de matrículas…</div>;

  return (
    <div className="management-grid">
      <section className="management-card">
        <span className="auth-eyebrow">Currículo</span>
        <h1>Matricular aluno</h1>
        <p>Somente cursos publicados ficam disponíveis na conta do aluno. Uma matrícula pausada ou cancelada bloqueia o currículo.</p>
        <form className="auth-form" onSubmit={createEnrollment}>
          <label htmlFor="enrollment-student">Aluno</label>
          <select id="enrollment-student" value={studentId} onChange={(event) => setStudentId(event.target.value)} required>
            {students.map((student) => <option value={student.id} key={student.id}>{student.name} · {student.email}</option>)}
          </select>
          <label htmlFor="enrollment-course">Curso publicado</label>
          <select id="enrollment-course" value={courseSlug} onChange={(event) => setCourseSlug(event.target.value)} required>
            {courses.map((course) => <option value={course.slug} key={course.slug}>{course.level} · {course.title}</option>)}
          </select>
          {!students.length ? <p className="form-error">Convide e ative um aluno antes de criar a matrícula.</p> : null}
          {error ? <p className="form-error" role="alert">{error}</p> : null}
          {message ? <p className="form-success" role="status">{message}</p> : null}
          <button type="submit" disabled={busy || !studentId || !courseSlug}>{busy ? "Matriculando…" : "Criar matrícula"}</button>
        </form>
      </section>

      <section className="enrollment-panel">
        <div><span className="auth-eyebrow">Matrículas existentes</span><h2>{enrollments.length} vínculo(s)</h2></div>
        <div className="enrollment-list">
          {enrollments.map((enrollment) => <article className="enrollment-row" key={enrollment.id}>
            <div><strong>{enrollment.student.name}</strong><span>{enrollment.student.email}</span><small>{enrollment.course.level} · {enrollment.course.title}</small></div>
            <label><span>Status</span><select value={enrollment.status} onChange={(event) => void changeStatus(enrollment, event.target.value as EnrollmentStatus)}>
              <option value="ACTIVE">Ativa</option>
              <option value="PAUSED">Pausada</option>
              <option value="COMPLETED">Concluída</option>
              <option value="CANCELLED">Cancelada</option>
            </select></label>
          </article>)}
          {!enrollments.length ? <p>Nenhuma matrícula criada.</p> : null}
        </div>
      </section>
    </div>
  );
}
