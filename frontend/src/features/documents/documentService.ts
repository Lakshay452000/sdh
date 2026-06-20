import { apiClient }
from "../../../src/services/apiClient";

import { appConfig }
from "../../config/appConfig";

import type {
  Document,
  UploadDocumentResponse
} from "./types";

export async function
getDocuments():
Promise<Document[]> {

  if (
    appConfig.mockMode
  ) {

    return [
      {
        document_id: "1",
        file_name:
          "Netflix.pdf"
      },
      {
        document_id: "2",
        file_name:
          "Uber.pdf"
      }
    ];
  }

  const response =
    await apiClient.get(
      "/documents"
    );

  return response.data;
}

export async function
uploadDocument(
  file: File
):
Promise<
  UploadDocumentResponse
> {

  if (
    appConfig.mockMode
  ) {

    return {

      document_id:
        crypto.randomUUID(),

      file_name:
        file.name,

      message:
        "Mock Upload Success"

    };
  }

  const formData =
    new FormData();

  formData.append(
    "file",
    file
  );

  const response =
    await apiClient.post(
      "/documents/upload",
      formData,
      {
        headers: {
          "Content-Type":
            "multipart/form-data"
        }
      }
    );

  return response.data;
}

export async function
deleteDocument(
  documentId: string
) {

  if (
    appConfig.mockMode
  ) {

    return;
  }

  await apiClient.delete(
    `/documents/${documentId}`
  );
}