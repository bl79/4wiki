# -*- coding: utf-8 -*-
import vladi_commons
from lxml import etree, html

file_html = ''

# html = vladi_commons.file_readtext(file_html)

htm = """
<ol class='references'>
	<li id="cite_note-.27.27Katz.27.27.E2.80.942002.E2.80.94.E2.80.9448-9">
		<b><a href="#cite_ref-.27.27Katz.27.27.E2.80.942002.E2.80.94.E2.80.9448_9-0">↑</a></b>
		<span class="reference-text">
			<a href="#CITEREFKatz2002" title=""><i>Katz</i>, 2002</a>, с. 48.
		</span>
	</li>
</ol>

<div style='mso-element:footnote' id=ftn554>
	<p class=MsoFootnoteText>
		<a style='mso-footnote-id:ftn554' href="#_ftnref554" name="_ftn554" title="">
			<span class=MsoFootnoteReference>
				<span style='font-size:12.0pt;mso-bidi-font-size:10.0pt'>*</span>
			</span>
		</a>
		<i>Cic.</i><span> Tusc. 5, 21, 61—62.</span>
	</p>
</div>

<div style='mso-element:footnote' id=ftn555>
	<p class=MsoFootnoteText>
		<a style='mso-footnote-id:ftn555' href="#_ftnref555" name="_ftn555" title="">
			<span class=MsoFootnoteReference><span style='font-size:12.0pt;mso-bidi-font-size:10.0pt'>**</span></span>
		</a>
		<span style='font-size:12.0pt;mso-bidi-font-size:10.0pt'> </span>
		<span style='font-size:9.0pt;mso-bidi-font-size:10.0pt;layout-grid-mode:line'>Т. е.
		предсказатель по гороскопу.</span>
	</p>
</div>

<div class="references-small" style="column-count:2;-moz-column-count:2;-webkit-column-count:2;">
<ol class="references">
<li id="cite_note-aysor-1"><span class="mw-cite-backlink">↑ <a href="#cite_ref-aysor_1-0"><span class="cite-accessibility-label">Перейти к: </span><sup><i><b>1</b></i></sup></a> <a href="#cite_ref-aysor_1-1"><sup><i><b>2</b></i></sup></a> <a href="#cite_ref-aysor_1-2"><sup><i><b>3</b></i></sup></a> <a href="#cite_ref-aysor_1-3"><sup><i><b>4</b></i></sup></a> <a href="#cite_ref-aysor_1-4"><sup><i><b>5</b></i></sup></a> <a href="#cite_ref-aysor_1-5"><sup><i><b>6</b></i></sup></a> <a href="#cite_ref-aysor_1-6"><sup><i><b>7</b></i></sup></a> <a href="#cite_ref-aysor_1-7"><sup><i><b>8</b></i></sup></a></span> <span class="reference-text"><span class="citation"><a rel="nofollow" class="external text" href="http://www.aysor.am/am/news/2011/06/17/rudolf-muradyan/299909">Исполняется 75 лет со дня рождения академика Рудольфа Мурадяна</a>&nbsp;<span class="ref-info" title="на армянском языке" style="font-size:85%; cursor:help; color:#888;">(арм.)</span>.  www.aysor.am (17&nbsp;июня 2011). <small>Проверено 18 августа 2015.</small></span></span></li>
<li id="cite_note-mgu-2"><b><a href="#cite_ref-mgu_2-0">↑</a></b> <span class="reference-text"><span class="citation"><a rel="nofollow" class="external text" href="http://upmsu.phys.msu.ru/abc1959.html">Список выпускников физического факультета МГУ 1959 года</a>.  Союз выпускников физического факультета МГУ. <small>Проверено 18 августа 2015.</small></span></span></li>
<li id="cite_note-.D0.95.D0.B6.D0.B5.D0.B3.D0.BE.D0.B4.D0.BD.D0.B8.D0.BA_.D0.91.D0.A1.D0.AD.E2.80.941989.E2.80.94.E2.80.94575-3"><span class="mw-cite-backlink">↑ <a href="#cite_ref-.D0.95.D0.B6.D0.B5.D0.B3.D0.BE.D0.B4.D0.BD.D0.B8.D0.BA_.D0.91.D0.A1.D0.AD.E2.80.941989.E2.80.94.E2.80.94575_3-0"><span class="cite-accessibility-label">Перейти к: </span><sup><i><b>1</b></i></sup></a> <a href="#cite_ref-.D0.95.D0.B6.D0.B5.D0.B3.D0.BE.D0.B4.D0.BD.D0.B8.D0.BA_.D0.91.D0.A1.D0.AD.E2.80.941989.E2.80.94.E2.80.94575_3-1"><sup><i><b>2</b></i></sup></a> <a href="#cite_ref-.D0.95.D0.B6.D0.B5.D0.B3.D0.BE.D0.B4.D0.BD.D0.B8.D0.BA_.D0.91.D0.A1.D0.AD.E2.80.941989.E2.80.94.E2.80.94575_3-2"><sup><i><b>3</b></i></sup></a> <a href="#cite_ref-.D0.95.D0.B6.D0.B5.D0.B3.D0.BE.D0.B4.D0.BD.D0.B8.D0.BA_.D0.91.D0.A1.D0.AD.E2.80.941989.E2.80.94.E2.80.94575_3-3"><sup><i><b>4</b></i></sup></a></span> <span class="reference-text"><a href="#CITEREF.D0.95.D0.B6.D0.B5.D0.B3.D0.BE.D0.B4.D0.BD.D0.B8.D0.BA_.D0.91.D0.A1.D0.AD1989">Ежегодник БСЭ, 1989</a>, с. 575.</span></li>
<li id="cite_note-dubna-4"><span class="mw-cite-backlink">↑ <a href="#cite_ref-dubna_4-0"><span class="cite-accessibility-label">Перейти к: </span><sup><i><b>1</b></i></sup></a> <a href="#cite_ref-dubna_4-1"><sup><i><b>2</b></i></sup></a> <a href="#cite_ref-dubna_4-2"><sup><i><b>3</b></i></sup></a> <a href="#cite_ref-dubna_4-3"><sup><i><b>4</b></i></sup></a></span> <span class="reference-text"><span class="citation"><i>Н. Н. Прислонов.</i> <a rel="nofollow" class="external text" href="http://dubna.org/p/?id=19524">Мурадян Рудольф Мурадович</a>.  dubna.org. <small>Проверено 18 августа 2015.</small></span></span></li>
<li id="cite_note-nas-5"><span class="mw-cite-backlink">↑ <a href="#cite_ref-nas_5-0"><span class="cite-accessibility-label">Перейти к: </span><sup><i><b>1</b></i></sup></a> <a href="#cite_ref-nas_5-1"><sup><i><b>2</b></i></sup></a></span> <span class="reference-text"><span class="citation"><a rel="nofollow" class="external text" href="http://www.sci.am/members.php?mid=174&amp;langid=3">Рудольф Мурадович Мурадян</a>.  <a href="/wiki/%D0%9D%D0%90%D0%9D_%D0%A0%D0%90" class="mw-redirect" title="НАН РА">Национальная академия наук РА</a>. <small>Проверено 18 августа 2015.</small></span></span></li>
<li id="cite_note-pap-6"><b><a href="#cite_ref-pap_6-0">↑</a></b> <span class="reference-text"><span class="citation"><a rel="nofollow" class="external text" href="http://www.casinapioiv.va/content/accademia/en/academicians/ordinary/muradyan.html">Rudolf Muradyan</a>&nbsp;<span class="ref-info" title="на английском языке" style="font-size:85%; cursor:help; color:#888;">(англ.)</span>.  <a href="/wiki/%D0%9F%D0%B0%D0%BF%D1%81%D0%BA%D0%B0%D1%8F_%D0%B0%D0%BA%D0%B0%D0%B4%D0%B5%D0%BC%D0%B8%D1%8F_%D0%BD%D0%B0%D1%83%D0%BA" title="Папская академия наук">Pontifical Academy of Sciences</a>. <small>Проверено 18 августа 2015.</small></span></span></li>
<li id="cite_note-ufba-7"><b><a href="#cite_ref-ufba_7-0">↑</a></b> <span class="reference-text"><span class="citation"><a rel="nofollow" class="external text" href="http://www.fis.ufba.br/dfes/pesquisa.htm">Grupos de pesquisa. Instituto de física</a>&nbsp;<span class="ref-info" title="на португальском языке" style="font-size:85%; cursor:help; color:#888;">(порт.)</span>.  www.fis.ufba.br. <small>Проверено 18 августа 2015.</small></span></span></li>
<li id="cite_note-tav-8"><span class="mw-cite-backlink">↑ <a href="#cite_ref-tav_8-0"><span class="cite-accessibility-label">Перейти к: </span><sup><i><b>1</b></i></sup></a> <a href="#cite_ref-tav_8-1"><sup><i><b>2</b></i></sup></a></span> <span class="reference-text"><span class="citation"><a rel="nofollow" class="external text" href="http://www.inr.ru/tavkhelidze/">Альберт Никифорович Тавхелидзе</a>.  <a href="/wiki/%D0%98%D0%BD%D1%81%D1%82%D0%B8%D1%82%D1%83%D1%82_%D1%8F%D0%B4%D0%B5%D1%80%D0%BD%D1%8B%D1%85_%D0%B8%D1%81%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B9_%D0%A0%D0%90%D0%9D" title="Институт ядерных исследований РАН">Институт ядерных исследований РАН</a>. <small>Проверено 18 августа 2015.</small></span></span></li>
<li id="cite_note-.D0.94.D1.83.D0.B1.D0.BD.D0.B0_.E2.80.94_.D0.BE.D1.81.D1.82.D1.80.D0.BE.D0.B2_.D1.81.D1.82.D0.B0.D0.B1.D0.B8.D0.BB.D1.8C.D0.BD.D0.BE.D1.81.D1.82.D0.B8.E2.80.942006.E2.80.94.E2.80.94579-9"><b><a href="#cite_ref-.D0.94.D1.83.D0.B1.D0.BD.D0.B0_.E2.80.94_.D0.BE.D1.81.D1.82.D1.80.D0.BE.D0.B2_.D1.81.D1.82.D0.B0.D0.B1.D0.B8.D0.BB.D1.8C.D0.BD.D0.BE.D1.81.D1.82.D0.B8.E2.80.942006.E2.80.94.E2.80.94579_9-0">↑</a></b> <span class="reference-text"><a href="#CITEREF.D0.94.D1.83.D0.B1.D0.BD.D0.B0_.E2.80.94_.D0.BE.D1.81.D1.82.D1.80.D0.BE.D0.B2_.D1.81.D1.82.D0.B0.D0.B1.D0.B8.D0.BB.D1.8C.D0.BD.D0.BE.D1.81.D1.82.D0.B82006">Дубна — остров стабильности, 2006</a>, с. 579.</span></li>
<li id="cite_note-.D0.94.D1.83.D0.B1.D0.BD.D0.B0_.E2.80.94_.D0.BE.D1.81.D1.82.D1.80.D0.BE.D0.B2_.D1.81.D1.82.D0.B0.D0.B1.D0.B8.D0.BB.D1.8C.D0.BD.D0.BE.D1.81.D1.82.D0.B8.E2.80.942006.E2.80.94.E2.80.94132-10"><b><a href="#cite_ref-.D0.94.D1.83.D0.B1.D0.BD.D0.B0_.E2.80.94_.D0.BE.D1.81.D1.82.D1.80.D0.BE.D0.B2_.D1.81.D1.82.D0.B0.D0.B1.D0.B8.D0.BB.D1.8C.D0.BD.D0.BE.D1.81.D1.82.D0.B8.E2.80.942006.E2.80.94.E2.80.94132_10-0">↑</a></b> <span class="reference-text"><a href="#CITEREF.D0.94.D1.83.D0.B1.D0.BD.D0.B0_.E2.80.94_.D0.BE.D1.81.D1.82.D1.80.D0.BE.D0.B2_.D1.81.D1.82.D0.B0.D0.B1.D0.B8.D0.BB.D1.8C.D0.BD.D0.BE.D1.81.D1.82.D0.B82006">Дубна — остров стабильности, 2006</a>, с. 132.</span></li>
<li id="cite_note-.D0.9A.D0.BE.D1.81.D0.BC.D0.B8.D1.87.D0.B5.D1.81.D0.BA.D0.B8.D0.B5_.D1.87.D0.B8.D1.81.D0.BB.D0.B0_.D0.B8_.D0.B2.D1.80.D0.B0.D1.89.D0.B5.D0.BD.D0.B8.D0.B5_.D0.BC.D0.B5.D1.82.D0.B0.D0.B3.D0.B0.D0.BB.D0.B0.D0.BA.D1.82.D0.B8.D0.BA.D0.B8.E2.80.941977.E2.80.94.E2.80.9466-11"><b><a href="#cite_ref-.D0.9A.D0.BE.D1.81.D0.BC.D0.B8.D1.87.D0.B5.D1.81.D0.BA.D0.B8.D0.B5_.D1.87.D0.B8.D1.81.D0.BB.D0.B0_.D0.B8_.D0.B2.D1.80.D0.B0.D1.89.D0.B5.D0.BD.D0.B8.D0.B5_.D0.BC.D0.B5.D1.82.D0.B0.D0.B3.D0.B0.D0.BB.D0.B0.D0.BA.D1.82.D0.B8.D0.BA.D0.B8.E2.80.941977.E2.80.94.E2.80.9466_11-0">↑</a></b> <span class="reference-text"><a href="#CITEREF.D0.9A.D0.BE.D1.81.D0.BC.D0.B8.D1.87.D0.B5.D1.81.D0.BA.D0.B8.D0.B5_.D1.87.D0.B8.D1.81.D0.BB.D0.B0_.D0.B8_.D0.B2.D1.80.D0.B0.D1.89.D0.B5.D0.BD.D0.B8.D0.B5_.D0.BC.D0.B5.D1.82.D0.B0.D0.B3.D0.B0.D0.BB.D0.B0.D0.BA.D1.82.D0.B8.D0.BA.D0.B81977" title="">Космические числа и вращение метагалактики, 1977</a>, с. 66.</span></li>
<li id="cite_note-.D0.A0.D0.B5.D1.88.D0.B5.D0.BD.D0.B8.D0.B5_.D0.B7.D0.B0.D0.B4.D0.B0.D1.87.D0.B8_.D0.BE_.C2.AB.D1.81.D0.BB.D1.83.D1.87.D0.B0.D0.B9.D0.BD.D1.8B.D1.85_.D0.B1.D0.BB.D1.83.D0.B6.D0.B4.D0.B0.D0.BD.D0.B8.D1.8F.D1.85.C2.BB_.D0.B2_.D0.BF.D1.80.D0.BE.D1.81.D1.82.D1.80.D0.B0.D0.BD.D1.81.D1.82.D0.B2.D0.B5_.D0.BF.D0.BE.D1.81.D1.82.D0.BE.D1.8F.D0.BD.D0.BD.D0.BE.D0.B9_.D0.BA.D1.80.D0.B8.D0.B2.D0.B8.D0.B7.D0.BD.D1.8B.E2.80.941970.E2.80.94.E2.80.94328-12"><b><a href="#cite_ref-.D0.A0.D0.B5.D1.88.D0.B5.D0.BD.D0.B8.D0.B5_.D0.B7.D0.B0.D0.B4.D0.B0.D1.87.D0.B8_.D0.BE_.C2.AB.D1.81.D0.BB.D1.83.D1.87.D0.B0.D0.B9.D0.BD.D1.8B.D1.85_.D0.B1.D0.BB.D1.83.D0.B6.D0.B4.D0.B0.D0.BD.D0.B8.D1.8F.D1.85.C2.BB_.D0.B2_.D0.BF.D1.80.D0.BE.D1.81.D1.82.D1.80.D0.B0.D0.BD.D1.81.D1.82.D0.B2.D0.B5_.D0.BF.D0.BE.D1.81.D1.82.D0.BE.D1.8F.D0.BD.D0.BD.D0.BE.D0.B9_.D0.BA.D1.80.D0.B8.D0.B2.D0.B8.D0.B7.D0.BD.D1.8B.E2.80.941970.E2.80.94.E2.80.94328_12-0">↑</a></b> <span class="reference-text"><a href="#CITEREF.D0.A0.D0.B5.D1.88.D0.B5.D0.BD.D0.B8.D0.B5_.D0.B7.D0.B0.D0.B4.D0.B0.D1.87.D0.B8_.D0.BE_.C2.AB.D1.81.D0.BB.D1.83.D1.87.D0.B0.D0.B9.D0.BD.D1.8B.D1.85_.D0.B1.D0.BB.D1.83.D0.B6.D0.B4.D0.B0.D0.BD.D0.B8.D1.8F.D1.85.C2.BB_.D0.B2_.D0.BF.D1.80.D0.BE.D1.81.D1.82.D1.80.D0.B0.D0.BD.D1.81.D1.82.D0.B2.D0.B5_.D0.BF.D0.BE.D1.81.D1.82.D0.BE.D1.8F.D0.BD.D0.BD.D0.BE.D0.B9_.D0.BA.D1.80.D0.B8.D0.B2.D0.B8.D0.B7.D0.BD.D1.8B1970" title="">Решение задачи о «случайных блужданиях» в пространстве постоянной кривизны, 1970</a>, с. 328.</span></li>
<li id="cite_note-.D0.9E_.D0.B4.D0.B8.D1.81.D0.BA.D1.80.D0.B5.D1.82.D0.BD.D1.8B.D1.85_.D0.BF.D0.BE.D0.B4.D0.B3.D1.80.D1.83.D0.BF.D0.BF.D0.B0.D1.85_.D1.82.D1.80.D0.B5.D1.85.D0.BC.D0.B5.D1.80.D0.BD.D0.BE.D0.B9_.D0.B3.D1.80.D1.83.D0.BF.D0.BF.D1.8B_.D0.B2.D1.80.D0.B0.D1.89.D0.B5.D0.BD.D0.B8.D0.B9.E2.80.941981.E2.80.94.E2.80.94335-13"><b><a href="#cite_ref-.D0.9E_.D0.B4.D0.B8.D1.81.D0.BA.D1.80.D0.B5.D1.82.D0.BD.D1.8B.D1.85_.D0.BF.D0.BE.D0.B4.D0.B3.D1.80.D1.83.D0.BF.D0.BF.D0.B0.D1.85_.D1.82.D1.80.D0.B5.D1.85.D0.BC.D0.B5.D1.80.D0.BD.D0.BE.D0.B9_.D0.B3.D1.80.D1.83.D0.BF.D0.BF.D1.8B_.D0.B2.D1.80.D0.B0.D1.89.D0.B5.D0.BD.D0.B8.D0.B9.E2.80.941981.E2.80.94.E2.80.94335_13-0">↑</a></b> <span class="reference-text"><a href="#CITEREF.D0.9E_.D0.B4.D0.B8.D1.81.D0.BA.D1.80.D0.B5.D1.82.D0.BD.D1.8B.D1.85_.D0.BF.D0.BE.D0.B4.D0.B3.D1.80.D1.83.D0.BF.D0.BF.D0.B0.D1.85_.D1.82.D1.80.D0.B5.D1.85.D0.BC.D0.B5.D1.80.D0.BD.D0.BE.D0.B9_.D0.B3.D1.80.D1.83.D0.BF.D0.BF.D1.8B_.D0.B2.D1.80.D0.B0.D1.89.D0.B5.D0.BD.D0.B8.D0.B91981" title="">О дискретных подгруппах трехмерной группы вращений, 1981</a>, с. 335.</span></li>
<li id="cite_note-.D0.A1.D1.82.D1.80.D1.83.D0.BA.D1.82.D1.83.D1.80.D0.B0_.D0.A5.D0.BE.D0.BF.D1.84.D0.B0_.D0.B2_.7F.27.22.60UNIQ--math-0000002F-QINU.60.22.27.7F-.D0.B0.D0.BB.D0.B3.D0.B5.D0.B1.D1.80.D0.B0.D1.85_.D0.9B.D0.B8_.E2.80.94_.D0.9D.D0.B0.D0.BC.D0.B1.D1.83.E2.80.941998.E2.80.94.E2.80.9487-14"><b><a href="#cite_ref-.D0.A1.D1.82.D1.80.D1.83.D0.BA.D1.82.D1.83.D1.80.D0.B0_.D0.A5.D0.BE.D0.BF.D1.84.D0.B0_.D0.B2_.7F.27.22.60UNIQ--math-0000002F-QINU.60.22.27.7F-.D0.B0.D0.BB.D0.B3.D0.B5.D0.B1.D1.80.D0.B0.D1.85_.D0.9B.D0.B8_.E2.80.94_.D0.9D.D0.B0.D0.BC.D0.B1.D1.83.E2.80.941998.E2.80.94.E2.80.9487_14-0">↑</a></b>
 <span class="reference-text">
 	<a href="#CITEREF.D0.A1.D1.82.D1.80.D1.83.D0.BA.D1.82.D1.83.D1.80.D0.B0_.D0.A5.D0.BE.D0.BF.D1.84.D0.B0_.D0.B2_-.D0.B0.D0.BB.D0.B3.D0.B5.D0.B1.D1.80.D0.B0.D1.85_.D0.9B.D0.B8_.E2.80.94_.D0.9D.D0.B0.D0.BC.D0.B1.D1.831998">
 	Структура Хопфа в
 	<span><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;">
 	 <math xmlns="http://www.w3.org/1998/Math/MathML">
	  <semantics>
		<mrow class="MJX-TeXAtom-ORD">
		  <mstyle displaystyle="true" scriptlevel="0">
			<mi>n</mi>
		  </mstyle>
		</mrow>
		<annotation encoding="application/x-tex">{\displaystyle n}</annotation>
	  </semantics>
	 </math>
 </span>
 <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/a601995d55609f2d9f5e233e36fbe9ea26011b3b" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:1.405ex; height:1.676ex;" alt="n">
</span>-алгебрах Ли — Намбу, 1998</a>, с. 87.</span>
</li>
<li id="cite_note-.D0.9E_.D0.BD.D0.BE.D0.B2.D0.BE.D0.B9_.D1.84.D0.BE.D1.80.D0.BC.D0.B5_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D1.8B_.D0.9C.D0.B5.D0.BD.D0.B4.D0.B5.D0.BB.D0.B5.D0.B5.D0.B2.D0.B0.E2.80.941990.E2.80.94.E2.80.94479-15"><b><a href="#cite_ref-.D0.9E_.D0.BD.D0.BE.D0.B2.D0.BE.D0.B9_.D1.84.D0.BE.D1.80.D0.BC.D0.B5_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D1.8B_.D0.9C.D0.B5.D0.BD.D0.B4.D0.B5.D0.BB.D0.B5.D0.B5.D0.B2.D0.B0.E2.80.941990.E2.80.94.E2.80.94479_15-0">↑</a></b> <span class="reference-text"><a href="#CITEREF.D0.9E_.D0.BD.D0.BE.D0.B2.D0.BE.D0.B9_.D1.84.D0.BE.D1.80.D0.BC.D0.B5_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D1.8B_.D0.9C.D0.B5.D0.BD.D0.B4.D0.B5.D0.BB.D0.B5.D0.B5.D0.B2.D0.B01990">О новой форме таблицы Менделеева, 1990</a>, с. 479.</span></li>
<li id="cite_note-.D0.9E_.D0.BD.D0.BE.D0.B2.D0.BE.D0.B9_.D1.84.D0.BE.D1.80.D0.BC.D0.B5_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D1.8B_.D0.9C.D0.B5.D0.BD.D0.B4.D0.B5.D0.BB.D0.B5.D0.B5.D0.B2.D0.B0.E2.80.941990.E2.80.94.E2.80.94481-16"><b><a href="#cite_ref-.D0.9E_.D0.BD.D0.BE.D0.B2.D0.BE.D0.B9_.D1.84.D0.BE.D1.80.D0.BC.D0.B5_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D1.8B_.D0.9C.D0.B5.D0.BD.D0.B4.D0.B5.D0.BB.D0.B5.D0.B5.D0.B2.D0.B0.E2.80.941990.E2.80.94.E2.80.94481_16-0">↑</a></b> <span class="reference-text"><a href="#CITEREF.D0.9E_.D0.BD.D0.BE.D0.B2.D0.BE.D0.B9_.D1.84.D0.BE.D1.80.D0.BC.D0.B5_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D1.8B_.D0.9C.D0.B5.D0.BD.D0.B4.D0.B5.D0.BB.D0.B5.D0.B5.D0.B2.D0.B01990">О новой форме таблицы Менделеева, 1990</a>, с. 481.</span></li>
<li id="cite_note-.D0.94.D1.83.D0.B1.D0.BD.D0.B0_.E2.80.94_.D0.BE.D1.81.D1.82.D1.80.D0.BE.D0.B2_.D1.81.D1.82.D0.B0.D0.B1.D0.B8.D0.BB.D1.8C.D0.BD.D0.BE.D1.81.D1.82.D0.B8.E2.80.942006.E2.80.94.E2.80.94582-17"><b><a href="#cite_ref-.D0.94.D1.83.D0.B1.D0.BD.D0.B0_.E2.80.94_.D0.BE.D1.81.D1.82.D1.80.D0.BE.D0.B2_.D1.81.D1.82.D0.B0.D0.B1.D0.B8.D0.BB.D1.8C.D0.BD.D0.BE.D1.81.D1.82.D0.B8.E2.80.942006.E2.80.94.E2.80.94582_17-0">↑</a></b> <span class="reference-text"><a href="#CITEREF.D0.94.D1.83.D0.B1.D0.BD.D0.B0_.E2.80.94_.D0.BE.D1.81.D1.82.D1.80.D0.BE.D0.B2_.D1.81.D1.82.D0.B0.D0.B1.D0.B8.D0.BB.D1.8C.D0.BD.D0.BE.D1.81.D1.82.D0.B82006">Дубна — остров стабильности, 2006</a>, с. 582.</span></li>
<li id="cite_note-.D0.94.D1.83.D0.B1.D0.BD.D0.B0_.E2.80.94_.D0.BE.D1.81.D1.82.D1.80.D0.BE.D0.B2_.D1.81.D1.82.D0.B0.D0.B1.D0.B8.D0.BB.D1.8C.D0.BD.D0.BE.D1.81.D1.82.D0.B8.E2.80.942006.E2.80.94.E2.80.94607-18"><b><a href="#cite_ref-.D0.94.D1.83.D0.B1.D0.BD.D0.B0_.E2.80.94_.D0.BE.D1.81.D1.82.D1.80.D0.BE.D0.B2_.D1.81.D1.82.D0.B0.D0.B1.D0.B8.D0.BB.D1.8C.D0.BD.D0.BE.D1.81.D1.82.D0.B8.E2.80.942006.E2.80.94.E2.80.94607_18-0">↑</a></b> <span class="reference-text"><a href="#CITEREF.D0.94.D1.83.D0.B1.D0.BD.D0.B0_.E2.80.94_.D0.BE.D1.81.D1.82.D1.80.D0.BE.D0.B2_.D1.81.D1.82.D0.B0.D0.B1.D0.B8.D0.BB.D1.8C.D0.BD.D0.BE.D1.81.D1.82.D0.B82006">Дубна — остров стабильности, 2006</a>, с. 607.</span></li>
<li id="cite_note-.D0.94.D1.83.D0.B1.D0.BD.D0.B0_.E2.80.94_.D0.BE.D1.81.D1.82.D1.80.D0.BE.D0.B2_.D1.81.D1.82.D0.B0.D0.B1.D0.B8.D0.BB.D1.8C.D0.BD.D0.BE.D1.81.D1.82.D0.B8.E2.80.942006.E2.80.94.E2.80.94599-19"><b><a href="#cite_ref-.D0.94.D1.83.D0.B1.D0.BD.D0.B0_.E2.80.94_.D0.BE.D1.81.D1.82.D1.80.D0.BE.D0.B2_.D1.81.D1.82.D0.B0.D0.B1.D0.B8.D0.BB.D1.8C.D0.BD.D0.BE.D1.81.D1.82.D0.B8.E2.80.942006.E2.80.94.E2.80.94599_19-0">↑</a></b> <span class="reference-text"><a href="#CITEREF.D0.94.D1.83.D0.B1.D0.BD.D0.B0_.E2.80.94_.D0.BE.D1.81.D1.82.D1.80.D0.BE.D0.B2_.D1.81.D1.82.D0.B0.D0.B1.D0.B8.D0.BB.D1.8C.D0.BD.D0.BE.D1.81.D1.82.D0.B82006">Дубна — остров стабильности, 2006</a>, с. 599.</span></li>
<li id="cite_note-.D0.94.D1.83.D0.B1.D0.BD.D0.B0_.E2.80.94_.D0.BE.D1.81.D1.82.D1.80.D0.BE.D0.B2_.D1.81.D1.82.D0.B0.D0.B1.D0.B8.D0.BB.D1.8C.D0.BD.D0.BE.D1.81.D1.82.D0.B8.E2.80.942006.E2.80.94.E2.80.94596-20"><b><a href="#cite_ref-.D0.94.D1.83.D0.B1.D0.BD.D0.B0_.E2.80.94_.D0.BE.D1.81.D1.82.D1.80.D0.BE.D0.B2_.D1.81.D1.82.D0.B0.D0.B1.D0.B8.D0.BB.D1.8C.D0.BD.D0.BE.D1.81.D1.82.D0.B8.E2.80.942006.E2.80.94.E2.80.94596_20-0">↑</a></b> <span class="reference-text"><a href="#CITEREF.D0.94.D1.83.D0.B1.D0.BD.D0.B0_.E2.80.94_.D0.BE.D1.81.D1.82.D1.80.D0.BE.D0.B2_.D1.81.D1.82.D0.B0.D0.B1.D0.B8.D0.BB.D1.8C.D0.BD.D0.BE.D1.81.D1.82.D0.B82006">Дубна — остров стабильности, 2006</a>, с. 596.</span></li>
</ol>
</div>
"""

html_parsed = etree.HTML(htm)
# html_parsed = etree.fromstring(htm)

import re


def cut_href(href):
	pos = href.find('CITEREF')
	if pos >= 0:
		return href[pos:]
	return False

p_ref_list = html_parsed.xpath("//ol[@class='references']/li")
for li in p_ref_list:
	span_list = li.xpath("./span[@class='reference-text']")
	for span in span_list:
		a_list = span.xpath("./descendant::a[contains(@href,'CITEREF')]")
		# y = a_list[0].text_content()
		for a in a_list:
			# a_text = a.xpath("./a/text()")[0].text_content()
			# a_text = a.text
			# at = html.tostring(a, pretty_print=True)
			at = str(etree.tostring(a, encoding='unicode'))
			# a_text = re.search(r'<a [^>]*>(.*?)</a>', str(at)).group(1)
			a_text_r = re.search(r'<a [^>]*>(.*?)</a>',  at, re.DOTALL)
			a_text = a_text_r.group(1)
			o = a.attrib['href']
			href_cut = cut_href(o)
			pass

# ref_list = html_parsed.xpath("//div[@style='mso-element:footnote']")
ref_list = html_parsed.xpath("//p[@class='MsoFootnoteText']/span[@class='MsoFootnoteReference']")
for ref in ref_list:
	# t = ref.findall("p[@class='MsoFootnoteText']/span")[0]
	# 	t = ref.xpath("./p[@class='MsoFootnoteText']/span")
	# t = t.text
	u = html.tostring(ref, pretty_print=True)
	# o = ref.text_content()
	pass
	# 	ref.tag = 'ref'
	# 	# ref = '<ref name="%s">' % ref.attrib['id']
	# 	print(ref)
# print(str(html_parsed))
# print(str(html))
# pass



# ref_list = html_parsed.xpath("//div[@style='mso-element:footnote']")
# for ref in ref_list:
# 	t = ref.xpath("./p[@class='MsoFootnoteText']/span")
# 	print(t)
# 	ref.tag = 'ref'
# 	# ref = '<ref name="%s">' % ref.attrib['id']
# 	print(ref)
# print(str(html_parsed))
# print(str(html))
pass