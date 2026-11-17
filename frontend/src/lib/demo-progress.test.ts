import { describe, expect, it } from "vitest";

import { progressStats } from "./demo-progress";

describe("progressStats", () => {
  it("derives XP and course percentage from distinct completed lessons", () => {
    const stats = progressStats(
      {
        completed: {
          hello: { score: 100, completedAt: "2026-01-01", xpAwarded: 60 },
          tobe: { score: 67, completedAt: "2026-01-02", xpAwarded: 75 },
        },
      },
      8,
    );

    expect(stats).toEqual({ completedCount: 2, xp: 135, percent: 25 });
  });
});
