import java.util.ArrayList;
import java.util.List;

// 가비지 컬렉션이 정상적으로 동작하는 코드
public class GC_leak_Pro {
      public static void main(String[] args) throws Exception {
            List<Integer> li = new ArrayList<>();
            for (int idx=1; true; idx++) {
                // for문의 idx가 n00번이 돌아올 때마다 li 변수를 새롭게 할당하므로 heap 사이즈를 넘치지 않음
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
}
