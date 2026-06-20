import {
  useEffect,
  useState
} from "react";

import {
  Box,
  Button,
  List,
  ListItem,
  ListItemText,
  Paper,
  Typography
} from "@mui/material";

import PageHeader from
  "../../shared/components/PageHeader";

import {
  deleteDocument,
  getDocuments,
  uploadDocument
} from "./documentService";

import type {
  Document
} from "./types";

export default function
DocumentsPage() {

  const [
    documents,
    setDocuments
  ] = useState<Document[]>([]);

  const [
    selectedFile,
    setSelectedFile
  ] = useState<File | null>(
    null
  );

  const loadDocuments =
    async () => {

      const data =
        await getDocuments();

      setDocuments(data);
    };

  useEffect(() => {

    loadDocuments();

  }, []);

  const handleUpload =
    async () => {

      if (
        !selectedFile
      ) {
        return;
      }

      const response =
        await uploadDocument(
          selectedFile
        );

      setDocuments([
        ...documents,
        {
          document_id:
            response.document_id,

          file_name:
            response.file_name
        }
      ]);

      setSelectedFile(
        null
      );
    };

  const handleDelete =
    async (
      documentId: string
    ) => {

      await deleteDocument(
        documentId
      );

      setDocuments(
        documents.filter(
          (document) =>
            document.document_id !==
            documentId
        )
      );
    };

  return (

    <Box>

      <PageHeader
        title="Documents"
        subtitle="
        Upload and manage
        knowledge documents."
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

          Select Document

          <input
            hidden
            type="file"
            accept=".pdf,.txt"
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
            mt: 2
          }}
        >
          {
            selectedFile?.name
          }
        </Typography>

        <Button
          sx={{
            mt: 2,
            ml: 2
          }}
          variant="contained"
          onClick={
            handleUpload
          }
          disabled={
            !selectedFile
          }
        >
          Upload
        </Button>

      </Paper>

      <Paper
        sx={{
          p: 3
        }}
      >

        <Typography
          variant="h6"
          gutterBottom
        >
          Uploaded Documents
        </Typography>

        <List>

          {
            documents.map(
              (
                document
              ) => (

                <ListItem
                  key={
                    document
                    .document_id
                  }
                  secondaryAction={

                    <Button
                      color="error"
                      onClick={() =>
                        handleDelete(
                          document
                          .document_id
                        )
                      }
                    >
                      Delete
                    </Button>

                  }
                >

                  <ListItemText
                    primary={
                      document
                      .file_name
                    }
                  />

                </ListItem>

              )
            )
          }

        </List>

      </Paper>

    </Box>

  );
}