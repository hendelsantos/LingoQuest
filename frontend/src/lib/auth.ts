export type UserRole = "ADMIN" | "TEACHER" | "STUDENT";

export type AuthUser = {
  id: string;
  email: string;
  name: string;
  role: UserRole;
};

type AuthResponse = {
  user: AuthUser;
  csrfToken: string;
};

type ErrorPayload = {
  detail?: string;
  [key: string]: unknown;
};

export class ApiError extends Error {
  constructor(
    message: string,
    readonly status: number,
    readonly payload?: ErrorPayload,
  ) {
    super(message);
  }
}

async function parseResponse<T>(response: Response): Promise<T> {
  const payload = (await response.json().catch(() => ({}))) as ErrorPayload;
  if (!response.ok) {
    const fieldError = Object.values(payload).find((value) =>
      Array.isArray(value) && typeof value[0] === "string"
    ) as string[] | undefined;
    throw new ApiError(
      payload.detail ?? fieldError?.[0] ?? "Não foi possível concluir a solicitação.",
      response.status,
      payload,
    );
  }
  return payload as T;
}

export async function getCsrfToken(): Promise<string> {
  const response = await fetch("/api/v1/auth/csrf/", {
    credentials: "same-origin",
    cache: "no-store",
  });
  return (await parseResponse<{ csrfToken: string }>(response)).csrfToken;
}

export async function apiPost<T>(path: string, body: object = {}): Promise<T> {
  const csrfToken = await getCsrfToken();
  const response = await fetch(path, {
    method: "POST",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify(body),
  });
  return parseResponse<T>(response);
}

export async function getCurrentUser(): Promise<AuthUser> {
  const response = await fetch("/api/v1/auth/me/", {
    credentials: "same-origin",
    cache: "no-store",
  });
  return parseResponse<AuthUser>(response);
}

export function destinationForRole(role: UserRole): string {
  if (role === "ADMIN") return "/school";
  if (role === "TEACHER") return "/teacher";
  return "/app";
}

export async function login(email: string, password: string): Promise<AuthResponse> {
  return apiPost<AuthResponse>("/api/v1/auth/login/", { email, password });
}
