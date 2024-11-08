package sudoku;
import java.util.Random;
import java.util.Scanner;

public class janken {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        // じゃんけんの手を数値で表す
        final int GUU = 0;
        final int CHOKI = 1;
        final int PA = 2;

        
        while (true) {
            System.out.print("じゃんけん！ (0:グー, 1:チョキ, 2:パー) >> ");
            int userHand = scanner.nextInt();

            // コンピュータの手をランダムに生成
            int computerHand = random.nextInt(3);

            // 勝敗判定
            if (userHand == computerHand) {
                System.out.println("あいこです！");
            } else if ((userHand == GUU && computerHand == CHOKI) ||
                       (userHand == CHOKI && computerHand == PA) ||
                       (userHand == PA && computerHand == GUU)) {
                System.out.println("あなたの勝ちです！");
            }else if(userHand == GUU || userHand == CHOKI || userHand == PA) {
                System.out.println("あなたの負けです・・");
            
            }else {
                System.out.println("不正です！0から2の数値を入力してください！");
            }

            System.out.print("もう一度やりますか？(y/n) >> ");
            String answer = scanner.next();
            if (answer.equals("n")) {
                break;
            }
        }
    }
}
