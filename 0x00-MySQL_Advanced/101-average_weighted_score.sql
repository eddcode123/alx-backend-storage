DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  -- First, ensure that the average_score column exists and has an appropriate data type.
  -- Example: ALTER TABLE users ADD COLUMN average_score DECIMAL(5,2);

  -- Perform the update operation
  UPDATE users AS U
  JOIN (
    SELECT U.id, SUM(score * weight) / NULLIF(SUM(weight), 0) AS w_avg
    FROM users AS U
    JOIN corrections AS C ON U.id = C.user_id
    JOIN projects AS P ON C.project_id = P.id
    GROUP BY U.id
  ) AS WA
  ON U.id = WA.id
  SET U.average_score = WA.w_avg;
END;
DELIMITER ;
