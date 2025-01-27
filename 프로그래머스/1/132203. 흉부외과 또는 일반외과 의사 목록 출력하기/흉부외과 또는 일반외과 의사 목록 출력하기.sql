-- 코드를 입력하세요
# 흉부외과 이거나 일반 외과인 의사 
# 이름, 의사 id, 진료과, 고용일자

SELECT DR_NAME, DR_ID, MCDP_CD, SUBSTR(HIRE_YMD,1,10)
FROM DOCTOR
WHERE (MCDP_CD = 'CS') OR (MCDP_CD = 'GS')
ORDER BY HIRE_YMD DESC, DR_NAME ASC