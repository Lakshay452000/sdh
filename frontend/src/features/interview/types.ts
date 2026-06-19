export type InterviewEvaluation = {
  strengths: string[];
  weaknesses: string[];
  missing_concepts: string[];
  score: number;
};

export type InterviewSession = {
  sessionId: string;
  currentQuestion: string;
};