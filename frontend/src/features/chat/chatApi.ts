import { apiClient } from "../../services/apiClient";

export async function askQuestion(
  question: string
) {

  const response =
    await apiClient.post(
      "/chat/ask",
      {
        session_id: "demo-session",
        question
      }
    );

  return response.data;
}