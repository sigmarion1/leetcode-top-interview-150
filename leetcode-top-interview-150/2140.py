class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # Recursive Way
        # if not questions:
        #     return 0

        # current_question = questions[0]

        # if len(questions) == 1:
        #     return current_question[0]

        # after_brainpower_question_index = current_question[1] + 1
        # after_brainpower_questions = []

        # if len(questions) > after_brainpower_question_index:
        #     after_brainpower_questions = questions[after_brainpower_question_index:]

        # skipped_questions = questions[1:]

        # return max(current_question[0] + self.mostPoints(after_brainpower_questions), self.mostPoints(skipped_questions))

        # Dynamic Program Way

        lq = len(questions)
        dp = [0] * (lq + 1)

        for i in range(lq - 1, -1, -1):
            pt, bp = questions[i]

            nxt = i + (bp + 1)

            if nxt > lq:
                nxt = lq

            dp[i] = max(dp[i + 1], pt + dp[nxt])

        return dp[0]
