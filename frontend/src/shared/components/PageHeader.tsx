import {
  Typography
} from "@mui/material";

type Props = {
  title: string;
  subtitle?: string;
};

export default function PageHeader(
  {
    title,
    subtitle
  }: Props
) {

  return (
    <>
      <Typography
        variant="h4"
        gutterBottom
      >
        {title}
      </Typography>

      {subtitle && (

        <Typography
          variant="body1"
          sx={{
            mb: 3
          }}
        >
          {subtitle}
        </Typography>

      )}
    </>
  );
}