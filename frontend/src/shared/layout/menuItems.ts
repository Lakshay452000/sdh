import ChatIcon from "@mui/icons-material/Chat";
import ArchitectureIcon from "@mui/icons-material/Architecture";
import RecordVoiceOverIcon from "@mui/icons-material/RecordVoiceOver";
import AnalyticsIcon from "@mui/icons-material/Analytics";
import DocumentIcon from "@mui/icons-material/DocumentScanner";

import { Permission } from "../../auth/permissions";

export const menuItems = [
  {
    label: "Chat",
    path: "/chat",
    icon: ChatIcon,
    permission: Permission.CHAT
  },
  {
    label: "Architecture Review",
    path: "/architecture",
    icon: ArchitectureIcon,
    permission: Permission.ARCHITECTURE
  },
  {
    label: "Interview",
    path: "/interview",
    icon: RecordVoiceOverIcon,
    permission: Permission.INTERVIEW
  },
  {
    label: "Evaluation",
    path: "/evaluation",
    icon: AnalyticsIcon,
    permission: Permission.EVALUATION
  },
  {
    label: "Documents",
    path: "/documents",
    icon: DocumentIcon,
    permission: Permission.DOCUMENTS
  }
];