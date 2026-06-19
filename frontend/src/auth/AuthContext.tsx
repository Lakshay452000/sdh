import {
  createContext,
  useContext,
  useState
} from "react";

import { Role } from "./roles";

type AuthContextType = {
  role: Role;
  setRole: (
    role: Role
  ) => void;
};

const AuthContext =
  createContext<AuthContextType | null>(
    null
  );

export function AuthProvider(
  {
    children
  }: {
    children: React.ReactNode;
  }
) {

  const [role, setRole] =
    useState<Role>(
      Role.USER
    );

  return (
    <AuthContext.Provider
      value={{
        role,
        setRole
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {

  const context =
    useContext(
      AuthContext
    );

  if (!context) {

    throw new Error(
      "AuthContext missing"
    );
  }

  return context;
}