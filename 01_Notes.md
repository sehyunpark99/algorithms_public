# Python

### Dynamic Programming

- Top-down: using recursion [call small qns for big qn]
  Use of memoization

  ```python
  # Fib
  # To mark that the qn has been solved or not
  d = [0] * 100

  def fibo(x):
  	# stop condition
  	if x == 1 or x == 2:
  		return 1
  	# if the qns once solved
  	if d[x] != 0:
  		return d[x]
  	d[x] = fibo(x-1) + fibo(x-2)
  	return d[x]
  ```
- Bottom-up: using iteration [solve small qns one by one]
- ```python
  d = [0] * 100
  d[1] = 1
  d[2] = 1
  n = 99

  for i in range(3, n+1):
  	d[i] = d[i-1] + d[i-2]

  ```

##### Substring vs Subsequence

In the context of strings:

1. **Substring** : A substring is a contiguous sequence of characters within a string. For example, in the string "hello", "ell" is a substring because the characters form a continuous sequence within the string.
2. **Subsequence** : A subsequence is a sequence that can be derived from another sequence by deleting zero or more elements without changing the order of the remaining elements. Unlike substrings, subsequences are not required to be contiguous. For example, in the string "hello", "ho" is a subsequence because the characters "h" and "o" appear in the same order as in the original string, but they are not contiguous.

In summary:

* Substrings are always contiguous.
* Subsequences may not be contiguous, but they preserve the order of characters from the original sequence.

### Heap

#### 파이썬 힙 자료구조

파이썬 heapq 모듈은 heapq (priority queue) 알고리즘을 제공한다.

모든 부모 노드는 그의 자식 노드보다 값이 작거나 큰 이진트리(binary tree) 구조인데, 내부적으로는 인덱스 0에서 시작해 k번째 원소가 항상 자식 원소들(2k+1, 2k+2) 보다 작거나 같은 **최소 힙**의 형태로 정렬된다.

heapq는 내장 모듈로 별도의 설치 작업 없이 바로 사용할 수 있다.

#### 힙 함수 활용하기

* heapq.heappush(heap, item) : item을 heap에 추가
* heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨.
* heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time,  *O(N) * )

### Linked List

### Problem List

- Merge Two Sorted Lists
- Merge k Sorted Lists
- Merge In Between Linked Lists

### How?

1. Dummy Linked List 만들기

   - merge한 값들을 저장하기 위함
   - 꼭 tail (실제로 이동하는 pointer) 만들기
   - dummy가 backup인 느낌이고 실제로 결과값을 반영하기 위한 도구는 tail
2. 내가 필요한 것에 따라 function을 추가한다

   - 두개를 이어줄 때 어떤 부분을 삭제해야 하면 Remove -CE.ipynb를 참고하여 노드간의 엣지를 cut해준다
   - 넣어주는 것은 tail.next 등을 이용해주기
3. while문의 조건에 주의하자

   - 이동하고 있는 tail.next (혹은 내가 assign하는 대상)이 None이 되지 않도록 while문을 짜야한다
   - 결국 바꿔주는 값들이 while문으로 value가 있는 범위에서 이동할 수 있도록 하는 것임.

### Graph

- Degree of a vertex
  - Undirected Graph: number of edges incident
  - Directed Graph
    - Indegree: edges go into the node
    - Outdegree: edges go away from node
- 

## Cycle Detection in Directed Graph

기본적으로 DFS를 이용해서 구한다.

원리는 DFS를 통해 방문을 시작한 vertex에 대해서 현재 stack안에 있다고 표시를 하고,

그 vertex의 방문이 완전 끝나면 stack에서 꺼낸다.

만약 어떤 vertex w를 방문했는데, 그 w가 stack안에 있으면, cycle이 생긴 것이다.

코드로 표현하면 다음과 같다.

|  | **private** **void** **dfs**(**LinkedList**<**Integer**>[]**adj**,**int** **v**) |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|  | {                                                                                                                                |
|  | **marked**[**v**] =**true**;                                                                                   |
|  | **onStack**[**v**] =**true**;                                                                                  |
|  |                                                                                                                                  |
|  | **for**(**int** **w**:**adj**[**v**])                                                              |
|  | {                                                                                                                                |
|  | **if**(**cycle**!=**null**)**return**;                                                                   |
|  |                                                                                                                                  |
|  | **if**(!**marked**[**w**])                                                                                     |
|  | {                                                                                                                                |
|  | **edgeTo**[**w**] =**v**;                                                                                      |
|  | **dfs**(**adj**,**w**);                                                                                        |
|  | }                                                                                                                                |
|  | **else** **if**(**onStack**[**w**])                                                                      |
|  | {                                                                                                                                |
|  | **cycle**=**new** **ArrayDeque**<**Integer**>();                                                         |
|  | **for**(**int** **x**=**v**;**x**!=**w**;**x**=**edgeTo**[**x**])                                  |
|  | **cycle**.**push**(**x**);                                                                                     |
|  | **cycle**.**push**(**w**);                                                                                     |
|  | **cycle**.**push**(**v**);                                                                                     |
|  | }                                                                                                                                |
|  | }                                                                                                                                |
|  |                                                                                                                                  |
|  | **onStack**[**v**] =**false**;                                                                                 |
|  | }                                                                                                                                |


## Cycle Detection in Undirected Graph

이것 또한 DFS를 이용해서 구현하는데, Directed Graph와는 조금 다르다.

왜냐하면, Undirected Graph는 기본적으로 양방향이기 때문에 위 구현 방법대로 하면 무조건 cycle이 생길 수 밖에 없다.

따라서 다른 방법을 이용해야하는데,

바로 dfs(adj, u, v). 바로 이전 vertex의 정보를 가지고 있는 거다.

그래서 v의 인접한 vertex들을 방문하면서 탐색할 때, vertex w를 방문했었는데, 그 vertex가 바로 이전 vertex u 와 다르다면 그것은 명백한 cycle이다.

코드로 표현하면 다음과 같다.

|  | **private** **dfs**(**LinkedList**<**Integer**>[]**adj**,**int** **u**,**int** **v**) |
| - | ------------------------------------------------------------------------------------------------------------------------------------------- |
|  | {                                                                                                                                           |
|  | **marked**[**v**] =**true**;                                                                                              |
|  | **for**(**int** **w**:**adj**[**v**])                                                                         |
|  | {                                                                                                                                           |
|  | **if**(**cycle**!=**null**)**return**;                                                                              |
|  |                                                                                                                                             |
|  | **if**(!**marked**[**w**])                                                                                                |
|  | {                                                                                                                                           |
|  | **edgeTo**[**w**] =**v**;                                                                                                 |
|  | **dfs**(**adj**,**v**,**w**);                                                                                       |
|  | }                                                                                                                                           |
|  | **else** **if**(**w**!=**u**)                                                                                       |
|  | {                                                                                                                                           |
|  | **cycle**=**new** **ArrayDeque**<**Integer**>();                                                                    |
|  | **for**(**int** **x**=**v**;**x**!=**w**;**x**=**edgeTo**[**x**])                                             |
|  | **cycle**.**push**(**x**);                                                                                                |
|  | **cycle**.**push**(**w**);                                                                                                |
|  | **cycle**.**push**(**x**);                                                                                                |
|  | }                                                                                                                                           |
|  | }                                                                                                                                           |
|  | }                                                                                                                                           |

# C

### [C] Malloc

###### **malloc 함수**

 - 동적으로 메모리를 할당하는 함수 (힙 영역에 메모리를 할당)

#include <stdlib.h>

void* malloc(size_t size)	// malloc 함수의 원형

함수 호출시 할당하고자 하는 메모리의 크기를 바이트 단위로 전달하면 그 크기만큼 메모리를 할당하게 된다.
그리고 할당한 메모리의 주소(첫 번째 바이트의 주소)를 리턴한다.
메모리 할당에 실패하면 NULL이 리턴된다.

리턴형이 void*(void 포인터) ??

malloc은 단순히 메모리만 할당하는 함수이기 때문에 개발자가 어떠한 데이터 형을 저장하는지 예측할 수 없다.
예를들어 4바이트를 할당하였을 경우 int형 데이터를 저장하기 위해서 사용하는지, float형 데이터를 사용하는지 예측할 수 없기 때문에 void포인터를 반환하여 개발자가 알맞은 용도로 변환하여 사용할 수 있도록 만든것이다.

예를들어 int형 데이터를 저장하기 위해서는 리턴되는 void*을 int*로 변환해야 한다.
int *i = (int*) malloc (sizeof(int));

위의 그림은 포인터 변수 i에 4바이트를 할당하는 그림이다.

1. sizeof(int)의 값은 4이다. 4라는 값을 전달하면서 malloc 함수를 호출한다.
2. 할당된 메모리의 주소가 void*형으로 리턴된다. 리턴되는 void*를 사용하려는 int*형으로 변환한다.
3. 포인터 변수 i에 대입한다.

###### **malloc함수 사용 예**

동적 할당을 사용하여 arr_1의 배열의 값을 대입하는 소스를 보며 malloc함수 사용법을 이해해보자.

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
	int arr_1[5];	// 배열 선언
	int *arr_2;		// 포인터 변수 선언
	int i;

    for(i = 0; i < 5; i++) {
		arr_1[i] = i+1;	// 배열에 값 대입
	}

    arr_2 = (int*) malloc(sizeof(int)*5);	// 메모리 할당, 배열의 크기만큼 할당하기 위해 5를 곱함

    for(i = 0; i < 5; i++) {
		arr_2[i] = arr_1[i];
		printf("%d ", arr_2[i]);
	}

    return 0;
}

    (adsbygoogle = window.adsbygoogle || []).push({});
```

###### **free 함수**

 - 힙 영역에 할당된 메모리를 해제하는 함수

메모리를 할당만 하고 해제해 주지 않는다면, 언젠가는 메모리가 부족한 현상이 발생 할 것이다.
할당된 메모리가 더 이상 필요하지 않을경우 free함수를 이용하여 메모리를 해제시켜 줘야한다.

```c
#include <stdlib.h>

void free(void* ptr)	// free 함수의 원형

free함수 사용 예
위의 예제에서 free함수만 추가시켰다.
#include <stdio.h>
#include <stdlib.h>

int main() {
	int arr_1[5];	// 배열 선언
	int *arr_2;		// 포인터 변수 선언
	int i;

    for(i = 0; i < 5; i++) {
		arr_1[i] = i+1;	// 배열에 값 대입
	}

    arr_2 = (int*) malloc(sizeof(int)*5);	// 메모리 할당, 배열의 크기만큼 할당하기 위해 5를 곱함

    for(i = 0; i < 5; i++) {
		arr_2[i] = arr_1[i];
		printf("%d ", arr_2[i]);
	}

    free(arr_2);	// free함수를 이용하여 메모리 해제

    return 0;
}

    (adsbygoogle = window.adsbygoogle || []).push({});
```

###### **calloc 함수**

 - calloc함수는 malloc함수와 같은 기능을 지니고 있다. 다만 사용하는 형태가 조금 다를 뿐이다.

```c
#include <stdlib.h>

void* calloc(size_t elt_count, size_t elt_size)	// calloc 함수 원형

calloc 함수는 elt_size 크기의 변수를 elt_count 개 만큼 저장할 수 있는 메모리 공간을 할당하라는 의미를 갖는다.

calloc함수 사용 예
위의 예제에서 malloc 함수대신 calloc 함수를 사용하였다.
#include <stdio.h>
#include <stdlib.h>

int main() {
	int arr_1[5];	// 배열 선언
	int *arr_2;		// 포인터 변수 선언
	int i;

    for(i = 0; i < 5; i++) {
		arr_1[i] = i+1;	// 배열에 값 대입
	}

    //arr_2 = (int*) malloc(sizeof(int)*5);	// 메모리 할당, 배열의 크기만큼 할당하기 위해 5를 곱함
	arr_2 = (int*) calloc(5, sizeof(int));	// sizoe(int)크기의 변수를 5개 저장할 수 있는 공간할당

    for(i = 0; i < 5; i++) {
		arr_2[i] = arr_1[i];
		printf("%d ", arr_2[i]);
	}

    free(arr_2);	// free함수를 이용하여 메모리 해제

    return 0;
}

malloc함수와 calloc함수의 차이점!
malloc은 할당된 공간의 값을은 바꾸지 않는다.
calloc은 할당된 공간의 값을 모두 0으로 바꾼다.
배열을 할당하고 모두 0으로 초기화할 필요가 있을경우에는 calloc을 쓰면 편하다.

    (adsbygoogle = window.adsbygoogle || []).push({});
```

###### **realloc 함수**

 - 이미 할당한 공간의 크기를 바꿀 때 realloc 함수를 사용한다.

```c


#include <stdlib.h>

void* realloc(void* memblock, size_t size);	// realloc 함수의 원형

이미 할당한 포인터 변수를 memblock에 넣고, 바꾸고 싶은 공간의 크기를 size에 입력하여 사용한다.

realloc함수 사용 예
malloc함수를 사용한 예제에서 realloc 함수를 사용하여 변경하였다.

#include <stdio.h>
#include <stdlib.h>

int main() {
	int arr_1[10];	// 배열 선언
	int *arr_2;		// 포인터 변수 선언
	int i;

    for(i = 0; i < 10; i++) {
		arr_1[i] = i+1;	// 배열에 값 대입
	}

    arr_2 = (int*) malloc(sizeof(int)*5);	// 메모리 할당, 배열의 크기만큼 할당하기 위해 5를 곱함

    for(i = 0; i < 5; i++) {
		arr_2[i] = arr_1[i];
		printf("%d ", arr_2[i]);
	}

    printf("\n");

    // sizeof(int) = 4바이트
	realloc(arr_2, sizeof(int)*10);	// arr_2의 메모리를 40바이트로 재 할당
	// arr_2의 메모리 크기 : 20바이트 -> 40바이트

    for(i = 0; i < 10; i++) {
		arr_2[i] = arr_1[i];
		printf("%d ", arr_2[i]);
	}

    free(arr_2);	// free함수를 이용하여 메모리 해제

    return 0;
}
```

### Segmentation Fault

1. null 값을 가리키는 포인터에 접근할 경우
2. 할당 받은 메모리 공간을 넘은 곳을 건드린 경우
3. 더 이상 존재하지 않는 메모리 영역을 가리킬 경우
4. read-only 표시 메모리 영역에 쓰려고 할 경우

### Pointer의 이해

```c
int *ptr_a; // 포인터를 선언할 때는 *를 쓴다
ptr_a; // 포인터 자체를 의미할 때는 *를 쓰지 않는다. 
*ptr_a; // 포인터가 가리키는 변수를 의미할 때는 *를 쓴다

```

* 포인터는 변수의 주솟값을 담는 변수 -> 포인터 자체도 변수 + 고유한 주솟값 있다
* double pointer
* ```
  int *ptr_a = &a; 이고 **ptr_ptr_a = &ptr_a;일 때
  1. *ptr_ptr_a == ptr_a
  2. **ptr_ptr_a == *ptr_a == a
  ```
