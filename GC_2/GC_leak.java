import java.util.ArrayList;
import java.util.List;

// 가비지 컬렉션 메모리 leak이 발생하는 코드
public class GC_leak {
      public static void main(String[] args) throws Exception {
            List<Integer> li = new ArrayList<>();
            for (int idx=1; true; idx++) {
                // 메모리 부족으로 JVM이 객체를 할당할 수 없고, 가비지 컬렉션이 가용 가능한 메모리를 할당할 수 없다는 에러 뜸
                // 이를 해결하기 위해서는 LI 변수의 객체에 대한 재할당을 해야한다.
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
}
