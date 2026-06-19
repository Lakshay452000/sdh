import { Navigate } from
  "react-router-dom";

import { useAuth } from
  "./AuthContext";

import { Permission } from
  "./permissions";

import { permissionMap } from
  "./permissionMap";

type Props = {
  permission: Permission;
  children: React.ReactNode;
};

export default function
ProtectedRoute(
  {
    permission,
    children
  }: Props
) {

  const { role } =
    useAuth();

  const allowedRoles =
    permissionMap[
      permission
    ];

  if (
    !allowedRoles.includes(
      role
    )
  ) {

    return (
      <Navigate
        to="/chat"
        replace
      />
    );
  }

  return <>{children}</>;
}