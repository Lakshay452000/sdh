export const Role = {
  USER: "USER",
  ADMIN: "ADMIN",
  DEVELOPER: "DEVELOPER"
} as const;

export type Role =
  (typeof Role)[keyof typeof Role];