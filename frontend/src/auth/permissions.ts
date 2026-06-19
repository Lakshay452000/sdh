export const Permission = {
  CHAT: "CHAT",
  ARCHITECTURE: "ARCHITECTURE",
  INTERVIEW: "INTERVIEW",
  EVALUATION: "EVALUATION"
} as const;

export type Permission =
  (typeof Permission)[keyof typeof Permission];