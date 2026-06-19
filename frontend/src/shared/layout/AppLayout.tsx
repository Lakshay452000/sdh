import {
  Outlet,
  Link,
  useLocation
} from "react-router-dom";

import {
  Box,
  Drawer,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Typography,
  Divider,
  FormControl,
  Select,
  MenuItem
} from "@mui/material";

import {
  useAuth
} from "../../auth/AuthContext";

import {
  Role
} from "../../auth/roles";

import {
  permissionMap
} from "../../auth/permissionMap";

import {
  menuItems
} from "./menuItems";

const drawerWidth = 260;

export default function AppLayout() {

  const location =
    useLocation();

  const {
    role,
    setRole
  } = useAuth();

  return (

    <Box
      sx={{
        display: "flex",
        minHeight: "100vh"
      }}
    >

      <Drawer
        variant="permanent"
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          "& .MuiDrawer-paper": {
            width: drawerWidth,
            boxSizing: "border-box"
          }
        }}
      >

        <Box
          sx={{
            p: 2
          }}
        >

          <Typography
            variant="h5"
          >
            SDH
          </Typography>

          <Typography
            variant="body2"
          >
            System Design Helper
          </Typography>

        </Box>

        <Divider />

        <Box
          sx={{
            p: 2
          }}
        >

          <Typography
            variant="body2"
            sx={{
              mb: 1
            }}
          >
            Role
          </Typography>

          <FormControl
            fullWidth
            size="small"
          >

            <Select
              value={role}
              onChange={(e) =>
                setRole(
                  e.target.value as Role
                )
              }
            >

              <MenuItem
                value={Role.USER}
              >
                USER
              </MenuItem>

              <MenuItem
                value={Role.ADMIN}
              >
                ADMIN
              </MenuItem>

              <MenuItem
                value={Role.DEVELOPER}
              >
                DEVELOPER
              </MenuItem>

            </Select>

          </FormControl>

        </Box>

        <Divider />

        <List>

          {menuItems
            .filter(
              (item) =>
                permissionMap[
                  item.permission
                ].includes(role)
            )
            .map(
              (item) => {

                const Icon =
                  item.icon;

                return (

                  <ListItemButton
                    key={
                      item.path
                    }
                    component={Link}
                    to={item.path}
                    selected={
                      location.pathname ===
                      item.path
                    }
                  >

                    <ListItemIcon>
                      <Icon />
                    </ListItemIcon>

                    <ListItemText
                      primary={
                        item.label
                      }
                    />

                  </ListItemButton>

                );
              }
            )}

        </List>

      </Drawer>

      <Box
        component="main"
        sx={{
          flexGrow: 1,
          p: 3
        }}
      >

        <Outlet />

      </Box>

    </Box>
  );
}