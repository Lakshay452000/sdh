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

export default function InterviewPage() {

  const [
    problemName,
    setProblemName
  ] = useState("");

  const [
    sessionStarted,
    setSessionStarted
  ] = useState(false);

  const [
    currentQuestion,
    setCurrentQuestion
  ] = useState("");

  const [
    answer,
    setAnswer
  ] = useState("");

  const [
    evaluation,
    setEvaluation
  ] = useState<any>(null);

  const startInterview =
    async () => {

      setSessionStarted(
        true
      );

      setCurrentQuestion(
        "Design Netflix."
      );
    };

  const submitAnswer =
    async () => {

      setEvaluation({
        score: 75,
        strengths: [
          "Good scalability discussion"
        ],
        weaknesses: [
          "Cache strategy missing"
        ],
        missing_concepts: [
          "CDN"
        ]
      });

      setCurrentQuestion(
        "How would you handle caching?"
      );

      setAnswer("");
    };

  return (

    <Box>

      <Typography
        variant="h4"
        gutterBottom
      >
        Interview Simulator
      </Typography>

      {!sessionStarted && (

        <Paper
          sx={{
            p: 3
          }}
        >

          <TextField
            fullWidth
            label="Problem Name"
            value={problemName}
            onChange={(e) =>
              setProblemName(
                e.target.value
              )
            }
          />

          <Button
            sx={{
              mt: 2
            }}
            variant="contained"
            onClick={startInterview}
          >
            Start Interview
          </Button>

        </Paper>

      )}

      {sessionStarted && (

        <>

          <Paper
            sx={{
              p: 2,
              mb: 2
            }}
          >

            <Typography
              variant="h6"
            >
              Question
            </Typography>

            <Typography>
              {currentQuestion}
            </Typography>

          </Paper>

          <TextField
            multiline
            rows={8}
            fullWidth
            label="Your Answer"
            value={answer}
            onChange={(e) =>
              setAnswer(
                e.target.value
              )
            }
          />

          <Button
            sx={{
              mt: 2
            }}
            variant="contained"
            onClick={submitAnswer}
          >
            Submit Answer
          </Button>

          {evaluation && (

            <Paper
              sx={{
                mt: 3,
                p: 2
              }}
            >

              <Typography
                variant="h6"
              >
                Evaluation
              </Typography>

              <Typography>
                Score:
                {" "}
                {evaluation.score}
              </Typography>

              <Typography
                sx={{
                  mt: 2
                }}
              >
                Strengths:
              </Typography>

              <ul>
                {
                  evaluation.strengths.map(
                    (
                      item: string
                    ) => (
                      <li
                        key={item}
                      >
                        {item}
                      </li>
                    )
                  )
                }
              </ul>

              <Typography>
                Weaknesses:
              </Typography>

              <ul>
                {
                  evaluation.weaknesses.map(
                    (
                      item: string
                    ) => (
                      <li
                        key={item}
                      >
                        {item}
                      </li>
                    )
                  )
                }
              </ul>

            </Paper>

          )}

        </>

      )}

    </Box>

  );
}