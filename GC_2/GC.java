// 언어 : Java

/* 
1. 가비지 컬렉션(Garbage Collection, GC)
   - 메모리 관리 기법 중 하나로 프로그램이 동적으로 할당했던 메모리 영역 중에서 필요없게 된 영역을 해제하는 기능이다.
   - 동적 할당된 메모리 영역 가운데 어떤 변수도 가리키지 않는 메모리 영역을 탐지하여 자동으로 해제하는 기법이다.
*/

/* 
2. 가비지 컬렉터(Garbage Collector)
   - 가비지 컬렉션을 수행하는 주체
*/

/*
3. 가비지 컬렉션의 필요성
   - 가비지 컬렉션을 이용하게 되면 프로그래머가 동적으로 할당한 메모리 영역 전체를 완벽하게 관리하지 않아도 되고, 버그나 불필요한 작업을 해소할 수 있는 장점이 있다.
     하지만, 동적으로 할당된 메모리가 사용되지 않는 경우엔 문제가 발생한다.
     메모리 해제 시점을 추적해야 하는데 비용이 들게 되고, 프로그래머가 수동으로 메모리 할당과 해제를 일일이 해줘야한다. 그러므로 가비지 컬렉션이 필요하다.
 */

 /*
4. 가비지 컬렉션의 동작 매커니즘
   - 가비지 컬렉션을 실행하기 위해 JVM이 애플리케이션의 실행을 멈추는 작업이다. 
   - GC가 실행될 때는 GC를 실행하는 쓰레드를 제외한 모든 쓰레드들의 작업이 중단되고, GC가 완료되면 작업이 재개된다. 
   - JVM에서 GC의 스케줄링을 담당하여 Java 개발자에게 메모리 관리의 부담을 덜어준다.
   - GC는 background에서 데몬 쓰레드로 돌며 더이상 사용되지 않는 객체들을 메모리에서 제거하여 효율적인 메모리 사용을 돕는다.

 * stack 영역
   - 정적으로 할당된 메모리 영역으로 기본타입의 데이터가 할당이 되고, Heap 영역에 할당된 Object 타입의 참조를 위한 값들이 Stack 영역에 할당


 * Heap 영역
   - 동적으로 할당된 메모리 영역으로 모든 Object 타입 및 new를 사용하여 객체를 생성하면 힙 영역에 저장한다.
   - Heap 영역은 Young과 Old 영역으로 설계되었다.

 * Young 영역(Young Generation)
   - Young 영역은 새롭게 생성된 객체가 할당되는 영역으로 대부분의 객체가 금방 연결되지 않는 상태가 되기 때문에 많은 객체가 Young 영역에 생성되었다가 사라지며 Young 영역에 대한 가비지 컬렉션을 Minor GC라고 부른다. 
   - Young 영역은 Eden, survivor 0, survivor 1 인 3가지로 나눠진다. 
   - Eden 영역은 new를 통해 새로 생성된 객체가 위치하며 정기적인 쓰레기 수집 후 살아남은 객체들을 Survivor 영역으로 보낸다. 
   - Survivor 0 / Survivor 1 영역은 최소 1번의 GC 이상 살아남은 객체가 존재하는 영역이며 Survivor 영역에는 특별한 규칙이 있는데 Survivor 0 / Survivor 1 둘 중 하나에는 꼭 비어 있어야 한다.
 
 *  Old 영역(Old Generation)
   - Old 영역은 Young 영역에서 연결되지 않는 상태를 유지하여 살아남은 객체가 복사되는 영역이다. Young 영역보다 크게 할당되고, 영역의 크기가 큰 만큼 가비지는 적게 발생하며 Old 영역에 대한 가비지 컬렉션을 Major GC 또는 Full GC라고 부른다.
 
 => 따라서 Young 영역의 수명이 짧은 객체들은 큰 공간을 필요하지 않으며 큰 객체들은 Old 영역에 할당되기 때문에 Old 영역이 Young 영역보다 크게 할당된다.
 
 
 => Young 영역과 Old 영역은 서로 다른 메모리 구조로 되어 있기 때문에 세부적인 동작 방식은 다르나, 기본적으로 가비지 컬렉션이 실행된다고 하면 2가지 공통적인 단계를 따른다.
 
 1. Stop The World
   - 가비지 컬렉션을 실행하기 위해 JVM이 애플리케이션의 실행을 멈추는 작업이다. 
     GC가 실행될 때는 GC를 실행하는 쓰레드를 제외한 모든 쓰레드들의 작업이 중단되고, GC가 완료되면 작업이 재개된다. 
     당연히 모든 쓰레드들의 작업이 중단되면 애플리케이션이 멈추기 때문에, GC의 성능 개선을 위해 튜닝을 한다고 하면 보통 stop-the-world의 시간을 줄이는 작업을 하는 것이다. 
     또한 JVM에서도 이러한 문제를 해결하기 위해 다양한 실행 옵션을 제공하고 있다.
 
 2. Mark and Sweep
   - Mark : 사용되는 메모리와 사용되지 않는 메모리를 식별하는 작업
   - Sweep : Mark 단계에서 사용되지 않음으로 식별된 메모리를 해제하는 작업
   - Stop The World를 통해 모든 작업을 중단시키면, GC는 스택의 모든 변수 또는 Reachable 객체를 스캔하면서 각각이 어떤 객체를 참고하고 있는지를 탐색하게 된다. 
     그리고 사용되고 있는 메모리를 식별하는데, 이러한 과정을 Mark라고 한다. 
     이후에 Mark가 되지 않은 객체들을 메모리에서 제거하는데, 이러한 과정을 Sweep라고 한다.
 
 * Minor GC의 동작 방식
  - Minor GC는 Eden 영역이 가득차거나, Survivor 영역, old 영역으로 객체를 재배치 할 때 발생하며 실행 속도가 빠르다.

 * Major GC의 동작 방식
  - Major GC는  Old 영역이 가득찬 경우 발생하며 실행 속도가 느리다.
 
 * GC 처리방식
  1. Serial GC
    - Mark-sweep-compact 알고리즘
    - 적은 메모리와 CPU 코어 갯수가 적을 때 적합하다.
  2. Paraller GC
    - Serial GC와 알고리즘은 같지만 GC를 처리하는 Thread가 여러개이다.
    - 메모리와 코어가 충분할 때 적합하다.
  3. Paraller Old GC
    - Paraller GC에서 Old GC 알고리즘을 개선한 버전이다.

 * 메모리 누수(Leak)
  - 자바에서 메모리 누수는 더 이상 사용되지 않는 객체들이 GC(가비지 컬렉션)에 의해 소멸되지 않고 누적되는 현상이다.
  - 가비지 컬렉션의 소멸 대상이 되려면 다른 Reference 변수에서 참조하고 있지 않아야 한다.

 * 가비지 컬렉션의 성능을 높이는 코딩 방법
    1. Collection의 크기를 예측하여 설정한다.
    2. Stream을 사용한다.
    3. String의 사용을 최적화한다.
    4. 불병성을 활용한다.
    5. 불필요한 Collection의 생성을 피한다.

   */

 /* 가비지 컬렉션 예제 코드
  1. 가비지 컬렉션이 제대로 동작하는 코드
  public static void main(String[] args) throws Exception {
          List<Integer> li = new ArrayList<>();
          for (int idx=1; true; idx++) {
              if (idx % 100 == 0) {
                li = new ArrayList<>();
                  Thread.sleep(100);
              }
              for(int k = 0; k < 100; k++){
                  li.add(k);
              }
              System.out.println("idx : "+ idx);
          }
  }

  2. 메모리 Leak이 발생하는 코드
  public static void main(String[] args) throws Exception {
        List<Integer> li = new ArrayList<>();
        for (int idx=1; true; idx++) {
            if (idx % 100 == 0) {
             //   li = new ArrayList<>();
                Thread.sleep(100);
            }
            for(int k = 0; k < 100; k++){
                li.add(k);
            }
            System.out.println("idx : "+ idx);
        }
}
   */
