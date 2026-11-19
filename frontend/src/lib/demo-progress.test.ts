import { describe, expect, it } from "vitest";

import { progressStats, reviewSchedule } from "./demo-progress";

describe("progressStats", () => {
  it("derives XP and course percentage from distinct completed lessons", () => {
    const stats = progressStats(
      {
        completed: {
          hello: { score: 100, completedAt: "2026-01-01", xpAwarded: 60, reviewedIntervals: [], lastReviewedAt: null },
          tobe: { score: 67, completedAt: "2026-01-02", xpAwarded: 75, reviewedIntervals: [], lastReviewedAt: null },
        },
        errors: {},
        assessments: {},
      },
      8,
    );

    expect(stats).toEqual({ completedCount: 2, xp: 135, percent: 25 });
  });

  it("schedules the first unfinished interval and marks overdue reviews", () => {
    const schedule = reviewSchedule(
      {
        completed: {
          hello: {
            score: 100,
            completedAt: "2026-01-01T12:00:00.000Z",
            xpAwarded: 60,
            reviewedIntervals: [1, 3],
            lastReviewedAt: "2026-01-04T12:00:00.000Z",
          },
        },
        errors: {},
        assessments: {},
      },
      new Date("2026-01-12T12:00:00.000Z"),
    );

    expect(schedule).toEqual([
      {
        slug: "hello",
        interval: 7,
        dueAt: "2026-01-11T12:00:00.000Z",
        due: true,
      },
    ]);
  });
});
