import {
  useState
} from "react";

import {
  Box,
  Button,
  Grid,
  Paper,
  TextField,
  Typography
} from "@mui/material";

import PageHeader from
  "../../shared/components/PageHeader";

import InfoCard from
  "../../shared/components/InfoCard";
  
export default function
ArchitecturePage() {

  const [
    description,
    setDescription
  ] = useState("");

  const [
    selectedFile,
    setSelectedFile
  ] = useState<File | null>(
    null
  );

  const [
    result,
    setResult
  ] = useState<any>(null);

  const runReview =
    async () => {

      setResult({
        review:
          "Mock review",

        evaluation:
          "Mock evaluation",

        correction:
          "Mock correction",

        verification:
          "Mock verification",

        mermaidDiagram:
          "graph TD; A-->B;"
      });
    };

  return (

    <Box>

      <PageHeader
      title="Architecture Review"
      subtitle="
      Upload an architecture diagram
      and get AI-powered review,
      evaluation and corrections."
    />

      <Paper
        sx={{
          p: 3,
          mb: 3
        }}
      >

        <Button
          variant="outlined"
          component="label"
        >

          Upload Diagram

          <input
            hidden
            type="file"
            accept="image/*"
            onChange={(e) =>
              setSelectedFile(
                e.target.files?.[0]
                ?? null
              )
            }
          />

        </Button>

        <Typography
          sx={{
            mt: 1
          }}
        >
          {
            selectedFile?.name
          }
        </Typography>

        <TextField
          multiline
          rows={6}
          fullWidth
          sx={{
            mt: 2
          }}
          label="Architecture Description"
          value={description}
          onChange={(e) =>
            setDescription(
              e.target.value
            )
          }
        />

        <Button
          sx={{
            mt: 2
          }}
          variant="contained"
          onClick={runReview}
        >
          Review Architecture
        </Button>

      </Paper>

      {result && (

        <Grid
          container
          spacing={2}
        >

          <Grid size={6}>

            <InfoCard
              title="Review"
            >
              {result.review}
            </InfoCard>

          </Grid>

          <Grid size={6}>

            <InfoCard
              title="Evaluation"
            >
              {result.evaluation}
            </InfoCard>

          </Grid>

          <Grid size={6}>

            <InfoCard
              title="Correction"
            >
              {result.correction}
            </InfoCard>

          </Grid>

          <Grid size={6}>

            <InfoCard
              title="Verification"
            >
              {result.verification}
            </InfoCard>

          </Grid>

          <Grid size={12}>

            <InfoCard
              title="Mermaid Diagram"
            >

              <pre>
                {
                  result
                  .mermaidDiagram
                }
              </pre>

            </InfoCard>

          </Grid>

        </Grid>

      )}

    </Box>
  );
}