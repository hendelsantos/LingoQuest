import { describe, expect, it } from "vitest";

import { site } from "./site";

describe("site metadata", () => {
  it("keeps the approved brand name and tagline", () => {
    expect(site).toEqual({
      name: "LingoQuest",
      tagline: "Small steps. Big adventures.",
    });
  });
});

