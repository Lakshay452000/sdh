import {
  Box,
  Grid,
  Paper,
  Typography
} from "@mui/material";

export default function
EvaluationPage() {

  const metrics = {

    faithfulness: 0.92,

    answerRelevancy: 0.88,

    contextPrecision: 0.90,

    contextRecall: 0.85

  };

  const overallScore = (
    (
      metrics.faithfulness +
      metrics.answerRelevancy +
      metrics.contextPrecision +
      metrics.contextRecall
    ) / 4
  ).toFixed(2);

  return (

    <Box>

      <Typography
        variant="h4"
        gutterBottom
      >
        Evaluation Dashboard
      </Typography>

      <Grid
        container
        spacing={2}
      >

        <Grid size={3}>
          <Paper sx={{ p: 2 }}>
            <Typography>
              Faithfulness
            </Typography>

            <Typography
              variant="h5"
            >
              {
                metrics
                .faithfulness
              }
            </Typography>
          </Paper>
        </Grid>

        <Grid size={3}>
          <Paper sx={{ p: 2 }}>
            <Typography>
              Answer Relevancy
            </Typography>

            <Typography
              variant="h5"
            >
              {
                metrics
                .answerRelevancy
              }
            </Typography>
          </Paper>
        </Grid>

        <Grid size={3}>
          <Paper sx={{ p: 2 }}>
            <Typography>
              Context Precision
            </Typography>

            <Typography
              variant="h5"
            >
              {
                metrics
                .contextPrecision
              }
            </Typography>
          </Paper>
        </Grid>

        <Grid size={3}>
          <Paper sx={{ p: 2 }}>
            <Typography>
              Context Recall
            </Typography>

            <Typography
              variant="h5"
            >
              {
                metrics
                .contextRecall
              }
            </Typography>
          </Paper>
        </Grid>

      </Grid>

      <Paper
        sx={{
          mt: 3,
          p: 2
        }}
      >

        <Typography
          variant="h6"
        >
          Overall Score
        </Typography>

        <Typography
          variant="h4"
        >
          {overallScore}
        </Typography>

      </Paper>

    </Box>
  );
}