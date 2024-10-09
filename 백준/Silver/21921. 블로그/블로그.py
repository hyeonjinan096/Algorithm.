import sys
input=sys.stdin.readline

N,X=map(int,input().split())
data=list(map(int,input().split()))

if max(data) == 0:
    print("SAD")
else:
	#value초기화
    value = sum(data[:X]) #X개씩 나눠서 sum
    
    max_value=value
    max_cnt=1

    for i in range(X,N):
    	#슬라이딩 윈도우진행
        value+=data[i] #슬라이딩윈도우 앞에
        #print("+",data[i])
        value-=data[i-X] #슬라이딩윈도우 뒤에값
        #print("-",data[i-X])

		#value의 최대값 찾음
        if value > max_value:
            max_value=value
            max_cnt=1
            
        #최대값 count    
        elif value == max_value:
            max_cnt+=1
    print(max_value)
    print(max_cnt)