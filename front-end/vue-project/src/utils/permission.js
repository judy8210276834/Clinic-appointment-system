const userPermissions = ['admin'];

export function usePermission() {
  const hasPermission = (permissions) => {
    return permissions.some(permission => userPermissions.includes(permission));
  };

  return {
    hasPermission
  };
}