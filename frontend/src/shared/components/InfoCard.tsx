import {
  Paper,
  Typography
} from "@mui/material";

type Props = {
  title: string;
  children: React.ReactNode;
};

export default function InfoCard(
  {
    title,
    children
  }: Props
) {

  return (
    <Paper
      sx={{
        p: 2,
        height: "100%"
      }}
    >
      <Typography
        variant="h6"
        gutterBottom
      >
        {title}
      </Typography>

      {children}

    </Paper>
  );
}