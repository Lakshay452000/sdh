import { Permission } from "./permissions";
import { Role } from "./roles";

export const permissionMap = {
  [Permission.CHAT]: [
    Role.USER,
    Role.ADMIN,
    Role.DEVELOPER
  ],

  [Permission.ARCHITECTURE]: [
    Role.USER,
    Role.ADMIN,
    Role.DEVELOPER
  ],

  [Permission.INTERVIEW]: [
    Role.USER,
    Role.ADMIN,
    Role.DEVELOPER
  ],

  [Permission.EVALUATION]: [
    Role.ADMIN,
    Role.DEVELOPER
  ],

  [Permission.DOCUMENTS]: [
    Role.ADMIN,
    Role.DEVELOPER
  ]
};