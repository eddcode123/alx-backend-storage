-- Script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans
SELECT origin FROM metal_bands
ORDER BY fans;
