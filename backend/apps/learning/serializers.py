from rest_framework import serializers

from apps.accounts.models import User

from .models import Course, Enrollment


class LessonSummarySerializer(serializers.Serializer):
    slug = serializers.SlugField()
    title = serializers.CharField()
    skill = serializers.CharField()
    summary = serializers.CharField()
    estimatedMinutes = serializers.IntegerField()
    xpReward = serializers.IntegerField()
    position = serializers.IntegerField()


class CourseUnitSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    position = serializers.IntegerField()
    lessons = LessonSummarySerializer(many=True)


class CourseOutlineSerializer(serializers.Serializer):
    slug = serializers.SlugField()
    title = serializers.CharField()
    description = serializers.CharField()
    level = serializers.CharField()
    lessonCount = serializers.IntegerField()
    units = CourseUnitSerializer(many=True)


class CourseSummarySerializer(serializers.Serializer):
    slug = serializers.SlugField()
    title = serializers.CharField()
    description = serializers.CharField()
    level = serializers.CharField()
    unitCount = serializers.IntegerField()
    lessonCount = serializers.IntegerField()


class LessonChoiceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.CharField()
    position = serializers.IntegerField()


class LessonQuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    type = serializers.CharField()
    prompt = serializers.CharField()
    position = serializers.IntegerField()
    choices = LessonChoiceSerializer(many=True, required=False)
    tokens = serializers.ListField(child=serializers.CharField(), required=False)
    audioText = serializers.CharField(required=False)


class DialogueLineSerializer(serializers.Serializer):
    speaker = serializers.CharField()
    line = serializers.CharField()


class ProductionTaskSerializer(serializers.Serializer):
    mode = serializers.ChoiceField(choices=("SPEAKING", "WRITING"))
    prompt = serializers.CharField()
    model = serializers.CharField()
    checklist = serializers.ListField(child=serializers.CharField())


class LessonPedagogySerializer(serializers.Serializer):
    objective = serializers.CharField()
    activationPrompt = serializers.CharField()
    commonMistakes = serializers.ListField(child=serializers.CharField())
    productionTask = ProductionTaskSerializer()
    reviewPrompts = serializers.ListField(child=serializers.CharField())


class LessonDetailSerializer(LessonSummarySerializer):
    unit = serializers.CharField()
    theory = serializers.CharField()
    example = serializers.CharField()
    keyPoints = serializers.ListField(child=serializers.CharField())
    dialogue = DialogueLineSerializer(many=True, required=False)
    pedagogy = LessonPedagogySerializer(required=False)
    passingPercent = serializers.IntegerField()
    questions = LessonQuestionSerializer(many=True)


class AnswerRequestSerializer(serializers.Serializer):
    questionId = serializers.IntegerField()
    choiceId = serializers.IntegerField(required=False)
    answer = serializers.CharField(required=False, allow_blank=True)
    order = serializers.ListField(
        child=serializers.CharField(), required=False, allow_empty=True
    )


class AnswerFeedbackSerializer(serializers.Serializer):
    isCorrect = serializers.BooleanField()
    explanation = serializers.CharField()
    selectedChoiceId = serializers.IntegerField(required=False)
    correctChoiceId = serializers.IntegerField(required=False)
    correctAnswer = serializers.CharField(required=False)
    errorCategory = serializers.ChoiceField(
        choices=(
            "GRAMMAR",
            "VOCABULARY",
            "WORD_ORDER",
            "LISTENING",
            "SPELLING",
            "COMPREHENSION",
        ),
        required=False,
    )


class AssessmentQuestionSerializer(serializers.Serializer):
    id = serializers.CharField()
    type = serializers.CharField()
    prompt = serializers.CharField()
    choices = serializers.ListField(child=serializers.CharField(), required=False)
    tokens = serializers.ListField(child=serializers.CharField(), required=False)
    audioText = serializers.CharField(required=False)


class AssessmentDetailSerializer(serializers.Serializer):
    moment = serializers.ChoiceField(choices=("initial", "final"))
    title = serializers.CharField()
    description = serializers.CharField()
    questions = AssessmentQuestionSerializer(many=True)
    speakingTask = serializers.CharField()
    writingTask = serializers.CharField()


class AssessmentAnswerSerializer(serializers.Serializer):
    questionId = serializers.CharField()
    choiceIndex = serializers.IntegerField(required=False)
    answer = serializers.CharField(required=False, allow_blank=True)
    order = serializers.ListField(child=serializers.CharField(), required=False)


class AssessmentFeedbackSerializer(serializers.Serializer):
    isCorrect = serializers.BooleanField()
    explanation = serializers.CharField()
    correctChoiceIndex = serializers.IntegerField(required=False)
    correctAnswer = serializers.CharField(required=False)
    errorCategory = serializers.CharField(required=False)


class EnrollmentStudentSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    email = serializers.EmailField()


class EnrollmentCourseSerializer(serializers.Serializer):
    slug = serializers.SlugField()
    title = serializers.CharField()
    level = serializers.CharField()


class EnrollmentSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    student = EnrollmentStudentSerializer()
    course = EnrollmentCourseSerializer()
    status = serializers.ChoiceField(choices=Enrollment.Status.choices)
    enrolledAt = serializers.DateTimeField()
    endedAt = serializers.DateTimeField(allow_null=True)


class EnrollmentCreateSerializer(serializers.Serializer):
    studentId = serializers.UUIDField()
    courseSlug = serializers.SlugField()

    def validate_studentId(self, value):
        student = User.objects.filter(id=value, role=User.Role.STUDENT).first()
        if student is None:
            raise serializers.ValidationError("Aluno inválido.")
        if not student.is_active:
            raise serializers.ValidationError("O aluno está desativado.")
        return value

    def validate_courseSlug(self, value):
        if not Course.objects.filter(slug=value, status=Course.Status.PUBLISHED).exists():
            raise serializers.ValidationError("Curso publicado não encontrado.")
        return value

    def validate(self, attrs):
        if Enrollment.objects.filter(
            student_id=attrs["studentId"], course__slug=attrs["courseSlug"]
        ).exists():
            raise serializers.ValidationError(
                {"courseSlug": "Este aluno já possui matrícula neste curso."}
            )
        return attrs


class EnrollmentStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Enrollment.Status.choices)
