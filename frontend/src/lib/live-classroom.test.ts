import { describe, expect, it } from "vitest";

import { checkClassroomAnswer, demoClassroomExercise } from "./live-classroom";

describe("checkClassroomAnswer", () => {
  it("accepts the correct answer without depending on case or whitespace", () => {
    expect(checkClassroomAnswer(demoClassroomExercise, " AM ")).toBe(true);
  });

  it("rejects an incorrect verb form", () => {
    expect(checkClassroomAnswer(demoClassroomExercise, "is")).toBe(false);
  });
});
