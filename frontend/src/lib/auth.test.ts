import { describe, expect, it } from "vitest";

import { destinationForRole } from "./auth";

describe("destinationForRole", () => {
  it.each([
    ["STUDENT", "/app"],
    ["TEACHER", "/teacher"],
    ["ADMIN", "/school"],
  ] as const)("sends %s to its protected area", (role, destination) => {
    expect(destinationForRole(role)).toBe(destination);
  });
});
