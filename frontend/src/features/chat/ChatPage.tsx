import {
  useState
} from "react";

import {
  Box,
  Button,
  Paper,
  TextField,
  Typography
} from "@mui/material";

import type { Message } from "./types";


export default function ChatPage() {

  const [question, setQuestion] =
    useState("");

  const [messages, setMessages] =
    useState<Message[]>([]);

  const handleAsk = async () => {

    if (!question.trim()) {
      return;
    }

    const userMessage: Message = {
      role: "user",
      content: question
    };

    setMessages(
      (prev) => [
        ...prev,
        userMessage
      ]
    );

    setQuestion("");

    // Temporary Mock

    setTimeout(() => {

      const assistantMessage: Message = {
        role: "assistant",
        content:
          "Mock response from SDH"
      };

      setMessages(
        (prev) => [
          ...prev,
          assistantMessage
        ]
      );

    }, 500);
  };

  return (

    <Box>

      <Typography
        variant="h4"
        gutterBottom
      >
        SDH Chat
      </Typography>

      <Paper
        sx={{
          height: "70vh",
          p: 2,
          mb: 2,
          overflowY: "auto"
        }}
      >

        {messages.map(
          (
            message,
            index
          ) => (

            <Box
              key={index}
              sx={{
                display: "flex",
                justifyContent:
                  message.role === "user"
                    ? "flex-end"
                    : "flex-start",
                mb: 2
              }}
            >

              <Paper
                sx={{
                  p: 2,
                  maxWidth: "70%"
                }}
              >

                {message.content}

              </Paper>

            </Box>

          )
        )}

      </Paper>

      <Box
        sx={{
          display: "flex",
          gap: 2
        }}
      >

        <TextField
          fullWidth
          value={question}
          onChange={(e) =>
            setQuestion(
              e.target.value
            )
          }
          label="Ask SDH"
        />

        <Button
          variant="contained"
          onClick={handleAsk}
        >
          Send
        </Button>

      </Box>

    </Box>
  );
}