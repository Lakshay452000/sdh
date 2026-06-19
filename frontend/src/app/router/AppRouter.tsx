import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
} from "react-router-dom";

import ChatPage from
  "../../features/chat/ChatPage";

import ArchitecturePage from
  "../../features/architecture/ArchitecturePage";

import InterviewPage from
  "../../features/interview/InterviewPage";

import EvaluationPage from
  "../../features/evaluation/EvaluationPage";

import AppLayout from
  "../../shared/layout/AppLayout";

export default function AppRouter() {

  return (
    <BrowserRouter>

      <Routes>

        <Route
          element={<AppLayout />}
        >

          <Route
            path="/"
            element={
              <Navigate
                to="/chat"
                replace
              />
            }
          />

          <Route
            path="/chat"
            element={<ChatPage />}
          />

          <Route
            path="/architecture"
            element={
              <ArchitecturePage />
            }
          />

          <Route
            path="/interview"
            element={<InterviewPage />}
          />

          <Route
            path="/evaluation"
            element={
              <EvaluationPage />
            }
          />

        </Route>

      </Routes>

    </BrowserRouter>
  );
}