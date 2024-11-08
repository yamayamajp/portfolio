#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>

int main(void) {
    setlocale(LC_ALL, "ja_JP.UTF-8");
    
    // 乱数の設定（randのみの場合、同じ乱数のシーケンスが繰り返される可能性あり）
    srand((unsigned int)time(NULL));

    // 1から100までの乱数を生成
    int answer = rand() % 100 + 1;

    // プレイヤーの入力を受け取るための変数
    int guess;
    int attempt = 0;  // 何回目の予想かをカウント

    printf("数当てゲームを始めます！\n");
    printf("1から100までの数を当ててください！\n");

    // 答えが当たるまで繰り返す
    do {
        printf("あなたの予想を入力してください: ");
        // 入力が整数かどうかをチェック
        if (scanf("%d", &guess) != 1) {
            // 整数以外の入力があった場合
            printf("無効な入力です。整数での入力をお願いします。\n");

            // 残っている無効なデータをクリア
            while (getchar() != '\n');  

            continue;  // 再度入力を促す
        }
        attempt++;

        if (guess < answer) {
            printf("もっと大きな数です。\n");

            // 予想と答えの差を使ってアドバイス
            if (answer - guess > 50) {
                printf("かなり小さいですね！もっと大きな数を試してみましょう。\n");
            } else if (answer - guess > 20) {
                printf("まだ少し小さいです。もう少し大きな数を試してみましょう。\n");
            }

        } else if (guess > answer) {
            printf("もっと小さな数です。\n");

            // 予想と答えの差を使ってアドバイス
            if (guess - answer > 50) {
                printf("かなり大きいですね！もっと小さな数を試してみましょう。\n");
            } else if (guess - answer > 20) {
                printf("まだ少し大きいです。もう少し小さな数を試してみましょう。\n");
            }
        }

    } while (guess != answer);

    printf("正解です！\n%d 回目で当たりました！\n", attempt);

    // 正解後、すぐにコンソールがすぐに閉じないようにする
    getchar();  
    printf("ゲームを終了します。\n終了するには何かキーを押してください...\n");
    getchar();  

    return 0;
}
