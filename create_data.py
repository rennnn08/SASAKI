from models.MySQL import MySQL

db = MySQL()

#ユーザを4人作成
print(db.regist_user('uS5qzaC2','Zi2WtFQ','田山　駿介','1'))
print(db.regist_user('スコット・J・ギルバード','Rf89Cnxh','S.J.G','4'))
print(db.regist_user('Joseph0425','D3qEbVs6','P.Parasite','2'))
print(db.regist_user('Sergio Carlo Di Benedetto','C7wBzfh4','@tanaka','0'))
print(db.regist_user('aaa','aaa','aaa','1'))

#質問の作成
print(db.regist_question('富士山の高さは何メートルですか？','雑学','富士山よりも大きな人になりたいです。','uS5qzaC2'))
print(db.regist_question('貧困層はなぜ増えるのですか？','社会','貧困層はなぜ増えるのですか？','スコット・J・ギルバード'))
print(db.regist_question('生活保護の申請方法がわかりません。','社会','生活保護の申請方法がわかりません。\n教えてください。','Joseph0425'))
print(db.regist_question('近所のピザがありえない','料理','ピザにコーンが乗っていて訳が分かりません。\n最近はこのようなピザが流行っているのですか？','Sergio Carlo Di Benedetto'))
print(db.regist_question('「り」から始まり「ん」で終わる言葉を教えてください。','宿題','「り」から始まり「ん」で終わる言葉を教えてください。','uS5qzaC2'))
print(db.regist_question('暑くて24時間ずっとエアコン点けっぱなしなんですが、エアコン壊れるでしょうか、、、','エアコン、空調家電','暑くて24時間ずっとエアコン点けっぱなしなんですが、エアコン壊れるでしょうか、、、','Joseph0425'))
print(db.regist_question('HDMIケーブルで接続すればパソコンの画面をテレビで見られるようになりますか？','パソコン','HDMIケーブルで接続すればパソコンの画面をテレビで見られるようになりますか？','Sergio Carlo Di Benedetto'))
print(db.regist_question('Core i シリーズとXeonはどちらの方が動画編集に向いていますか？','パソコン','Core i シリーズとXeonはどちらの方が動画編集に向いていますか？','uS5qzaC2'))
print(db.regist_question('コバエを退治するのにいい方法はありますか？','掃除','コバエを退治するのにいい方法はありますか？','スコット・J・ギルバード'))
print(db.regist_question('高いfpsを出すにはcpuにも関係ありますか？','パソコン','高いfpsを出すにはcpuにも関係ありますか？','uS5qzaC2'))
print(db.regist_question('バグが発生しています。','C言語',"""バグが発生しており、直し方がわかりません。教えてください。\npackage com.example.demo.controller;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.example.demo.entity.TestEntity;
import com.example.demo.pagination.PaginationObject;
import com.example.demo.pagination.SearchForm;
import com.example.demo.service.TestService;

@Controller
@RequestMapping(value = "/lesson2")
public class TestController {

    private static final String VIEW = "ResultDisplay";

    @GetMapping("/search")
        public String startdisplay(){
            return "BeginDisplay";
        }

        @Autowired
        public TestService testservice;

        @Autowired
        HttpSession session;


        @PostMapping("/search")
        public ModelAndView search( ModelAndView mov,
                @ModelAttribute SearchForm form,
                Pageable pageable
                ) {
               Page<TestEntity> resultdata = testservice.searchmaterial(form.getPage(),form.getTitle(),form.getTitleKana());
               mov.setViewName(VIEW);
               mov.addObject("form",form);
                mov.addObject("result",resultdata);
                mov.addObject("resultSize", resultdata.getSize());
                mov.addObject("page",PaginationObject. createPagenation(resultdata));
                return mov;
        }

}""",'Joseph0425'))
print(db.regist_question('広告の×などのマークが表示されたら自動で押すソフトか...','アプリ開発','広告のバツなどのマークが表示されたら自動で押すソフトかアプリはありますか？','Sergio Carlo Di Benedetto'))
print(db.regist_question('エクセル　マクロについて','Excel',"""
エクセル マクロについて

セル『B35~AJ47』に写真が複数貼り付けてあるんですが、一度に消す方法を教えて下さい
指定した箇所だけ消す方法を教えて下さい
よろしくお願いします
""",'スコット・J・ギルバード'))
print(db.regist_question('構造体ポインタってなんですか？何に使うんで...','C言語','構造体ポインタってなんですか？何に使うんですか？\n普通の変数ポインタとの違いはなんですか？','Sergio Carlo Di Benedetto'))
print(db.regist_question('ラーメンは日本料理ですか？中華料理ですか？','料理','ラーメンは日本料理ですか？中華料理ですか？','Joseph0425'))
print(db.regist_question('こんにちは天ぷらそばの天ぷら...','料理','こんにちは天ぷらそばの天ぷらといえばやっぱりエビでしょうか？？？','スコット・J・ギルバード'))
print(db.regist_question('コカ・コーラとコカ・コーラゼロに味の差は有りますか？','料理','コカ・コーラとコカ・コーラゼロに味の差は有りますか？','Sergio Carlo Di Benedetto'))
print(db.regist_question('納豆が食べれない人いますか？','料理','納豆が食べれない人いますか？','uS5qzaC2'))
print(db.regist_question('料理を作ると作りすぎてしまう人いますか？','料理','料理を作ると作りすぎてしまう人いますか？','Sergio Carlo Di Benedetto'))



#コピペ用
#print(db.regist_question('タイトル','カテゴリ','内容','回答者'))


#回答の作成
print(db.regist_answer(1,'8848メートルです','スコット・J・ギルバード'))
print(db.regist_answer(1,'3776メートルです','Sergio Carlo Di Benedetto'))
print(db.regist_answer(2,'なんとなくです','Joseph0425'))
print(db.regist_answer(3,'区役所にでも行ってください','uS5qzaC2'))
print(db.regist_answer(5,'梨園、離縁、罹患、離婚、リジン \n利点、理念、リボン、裏面、リヨン \n力点、陸軍、リスボン、リターン、立案 \nリムジン、リモコン、旅館、リリヤン、リン酸 \n隣人、鱗粉、リズム感、立春、リフレイン \n溜飲、硫酸、留年、料金、良品 \nリンパ腺、リアクション、領事館、龍馬伝 \n旅行券、理路整然、竜王戦、リロケーション、臨場感\nリアス式海岸、リハビリテーシヨン','スコット・J・ギルバード'))
print(db.regist_answer(6,'不良品や低価格品、怪しいメーカーじゃない限り壊れません\n\n余程、温度調整とかでエアコンをガチャガチャいじらなければの話ですが。','Sergio Carlo Di Benedetto'))
print(db.regist_answer(12,'>広告のバツなどのマークが表示されたら自動で押すソフトかアプリ\n\n広告は面倒だと思うでしょう\n私もそう思います\n\nではアプリが１個数千円だと買いますか\n広告にするので少し我慢すれば無料で見られるわけです','uS5qzaC2'))
print(db.regist_answer(12,"""
ありません。
広告ブロッカーをインストールすれば済むものを、わざわざ「×を押す」という動作を指せる意味はないためです。

なお、「広告かどうか」を100%確実に認識する技術は人類にはありませんので、この世のあらゆる広告を確実にブロックできる広告ブロッカーはありません。

それでよければ、一般的な広告であれば一般的なブロッカーでブロックできます。
""",'Joseph0425'))
print(db.regist_answer(13,"""『B35~AJ47』範囲内の画像(Picture)だけを削除します。テキストボックスや図形などは残します。


Sub test()
Dim sp As Shape
For Each sp In ActiveSheet.Shapes
If Not Intersect(sp.TopLeftCell, Range("B35:AJ47")) Is Nothing Then
If sp.Type = msoPicture Then
sp.Delete
End If
End If
Next
End Sub
""",'Joseph0425'))
print(db.regist_answer(13,"""B35：AJ47の範囲内にあるシェイプを削除します。

Sub test()
Dim HRng As Range, Rng As Range, r As Range
Dim Shp As Shape

Set HRng = Range("B35:AJ47")

For Each Rng In HRng
For Each Shp In ActiveSheet.Shapes
Set r = Range(Shp.TopLeftCell, Shp.BottomRightCell)
If Not Intersect(r, Rng) Is Nothing Then
Shp.Delete
End If
Next
Next

End Sub
""",'Sergio Carlo Di Benedetto'))
print(db.regist_answer(14,""">構造体ポインタってなんですか？
「その構造体型の」変数を指すポインタです

>何に使うんですか？
何に使うかは作る人の自由です
「普通の変数」ポインタと同じように必要に応じて使います

>普通の変数ポインタとの違いはなんですか？
同じです


何も特別なことはありません
「全ての型」に対してポインタは作れます
もちろんポインタのポインタも作れます
""",'Joseph0425'))



#コピペ用
#print(db.regist_answer(1,'回答内容','名前'))

