# -*- coding: utf-8 -*-
from lxml import etree
from io import StringIO

txt = """
<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.10/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.10/ http://www.mediawiki.org/xml/export-0.10.xsd" version="0.10" xml:lang="ru">
  <siteinfo>
    <sitename>Викитека</sitename>
    <dbname>ruwikisource</dbname>
    <base>https://ru.wikisource.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0</base>
    <generator>MediaWiki 1.31.0-wmf.22</generator>
    <case>first-letter</case>
    <namespaces>
      <namespace key="-2" case="first-letter">Медиа</namespace>
      <namespace key="-1" case="first-letter">Служебная</namespace>
      <namespace key="0" case="first-letter" />
      <namespace key="1" case="first-letter">Обсуждение</namespace>
      <namespace key="2" case="first-letter">Участник</namespace>
      <namespace key="3" case="first-letter">Обсуждение участника</namespace>
      <namespace key="4" case="first-letter">Викитека</namespace>
      <namespace key="5" case="first-letter">Обсуждение Викитеки</namespace>
      <namespace key="6" case="first-letter">Файл</namespace>
      <namespace key="7" case="first-letter">Обсуждение файла</namespace>
      <namespace key="8" case="first-letter">MediaWiki</namespace>
      <namespace key="9" case="first-letter">Обсуждение MediaWiki</namespace>
      <namespace key="10" case="first-letter">Шаблон</namespace>
      <namespace key="11" case="first-letter">Обсуждение шаблона</namespace>
      <namespace key="12" case="first-letter">Справка</namespace>
      <namespace key="13" case="first-letter">Обсуждение справки</namespace>
      <namespace key="14" case="first-letter">Категория</namespace>
      <namespace key="15" case="first-letter">Обсуждение категории</namespace>
      <namespace key="104" case="first-letter">Страница</namespace>
      <namespace key="105" case="first-letter">Обсуждение страницы</namespace>
      <namespace key="106" case="first-letter">Индекс</namespace>
      <namespace key="107" case="first-letter">Обсуждение индекса</namespace>
      <namespace key="108" case="first-letter">Импортировано</namespace>
      <namespace key="109" case="first-letter">Обсуждение импортированного</namespace>
      <namespace key="828" case="first-letter">Модуль</namespace>
      <namespace key="829" case="first-letter">Обсуждение модуля</namespace>
      <namespace key="2300" case="first-letter">Gadget</namespace>
      <namespace key="2301" case="first-letter">Gadget talk</namespace>
      <namespace key="2302" case="case-sensitive">Gadget definition</namespace>
      <namespace key="2303" case="case-sensitive">Gadget definition talk</namespace>
      <namespace key="2600" case="first-letter">Тема</namespace>
    </namespaces>
  </siteinfo>
  <page>
    <title>MediaWiki:Monobook.css</title>
    <ns>8</ns>
    <id>3</id>
    <revision>
      <id>944015</id>
      <parentid>905093</parentid>
      <timestamp>2012-11-30T10:56:36Z</timestamp>
      <contributor>
        <username>Lozman</username>
        <id>607</id>
      </contributor>
      <model>css</model>
      <format>text/css</format>
      <text xml:space="preserve">a { text-decoration: none }

/* Donations link to be uncommented during fundraising drives  */
#siteNotice {
    margin-top:5px;
    padding-left: 4px;
    font-style: italic;
    text-align: center;
}

#p-cactions { width: 80%; }
    /* patch to prevent vertical stacking of tabs
    at top of page in IE6 at resolutions of 800x600;
    this stacking occured in main namespace pages only
    for sysops, as they have the additional &quot;protect&quot;
    and &quot;delete&quot; tabs at the top of the page;
    original width before patch was 76%;
    this patch prevents stacking in main namespace pages
    but not in certain special pages,
    which have tabs that are of greater width --Lowellian */

/****************************/
/* BEGIN LIGHT BLUE SECTION */
/****************************/
/* Make all non-namespace pages have a light blue content area. This is done by
   setting the background color for all #content areas to light blue and then
   overriding it for any #content enclosed in a .ns-0 (main namespace). I then
   do the same for the &quot;tab&quot; background colors. --Lupo */

#content {
    background: #F8FCFF; /* a light blue */
}

#content div.thumb {
    border-color: #F8FCFF;
}

.ns-0 * #content {
    background: white;
}

#mytabs li {
    background: #F8FCFF;
}

.ns-0 * #mytabs li {
    background: white;
}

#mytabs li a {
    background-color: #F8FCFF;
}

.ns-0 * #mytabs li a {
    background-color: white;
}

#p-cactions li {
    background: #F8FCFF;
}

.ns-0 * #p-cactions li {
    background: white;
}

#p-cactions li a {
    background-color: #F8FCFF;
}

.ns-0 * #p-cactions li a {
    background-color: white;
}

.ns-0 * #content div.thumb {
    border-color: white;
}

/**************************/
/* END LIGHT BLUE SECTION */
/**************************/



#bodyContent #siteSub a {
    color: #000;
    text-decoration: none;
    background-color: transparent;
    background-image: none;
    padding-right: 0;
}


@media print {
    /* Do not print edit link in templates using Template:Ed
       Do not print certain classes that shouldn't appear on paper */
    .editlink, .noprint, .metadata, .dablink { display: none }
}

/* Style for &quot;notices&quot; */
.notice {
    text-align: justify;
    margin: 1em 0.5em;
    padding: 0.5em;
}

#disambig {
    border-top: 3px double #cccccc; 
    border-bottom: 3px double #cccccc;
}

/* extra buttons for edit dialog (from bg:)*/

 #my-buttons {
   padding: 0.5em;
 }
 #my-buttons a {
   color: black;
   background-color: #ccddee;
   font-weight: bold;
   font-size: 0.9em;
   text-decoration: none;
   border: thin #006699 outset;
   padding: 0 0.1em 0.1em 0.1em;
 }
 #my-buttons a:hover, #my-buttons a:active {
   background-color: #bbccdd;
   border-style: inset;
 }


/* by SergV */

@media print {
   /* Bug 1583 */
   .tright {clear: right;}
   /* рамка вокруг навигационных шаблонов */
   .toccolours {border: 1px solid #aaa;}
   /* линия над списком категорий */
   #catlinks {
       border-top: 1px solid black;
       margin-top: 1em;
       clear: both;
   }
}

/* Verse */

.verse {
	padding-left: 5em;
}

.verse pre {
        margin: 0;
        margin-bottom: -0.8em;
        margin-top: -0.8em;
        font-size: 100%;
        font-family: sans-serif;
	border: 0px;
	color: inherit;
	background-color: #ffffff;
	line-height: 150%;
}

.verse h2, .verse h3, .verse h4, .verse h5 {
	padding-left: 3em;
        text-align: left;
}

.verse p {
	padding-left: 1em;
        text-align: left;
}

/* Шаблон:PageQuality. Фон страницы в зависимости от ее статуса. */
.quality4 { background-color: #90ff90; }
.quality3 { background-color: #ffe867; }
.quality2 { background-color: #b0b0ff; }
.quality1 { background-color: #ffa0a0; }


TABLE { background-color: transparent }
TH { background-color: transparent }
TD { background-color: transparent }

/* Знак Ять на страницах в ДО */
div#pre-reform {
    position:absolute; 
    z-index:100; 
    right:10px; 
    top:10px;
}

#firstHeading .editsection {
    float:right;
    margin-left:5px;
}</text>
      <sha1>kglh9egu6xo5ck06xanbqxlbpns3nrc</sha1>
    </revision>
  </page>
  <page>
    <title>MediaWiki:Monobook.js</title>
    <ns>8</ns>
    <id>4</id>
    <revision>
      <id>2901740</id>
      <parentid>2325734</parentid>
      <timestamp>2017-10-26T22:39:00Z</timestamp>
      <contributor>
        <username>Lozman</username>
        <id>607</id>
      </contributor>
      <model>javascript</model>
      <format>text/javascript</format>
      <text xml:space="preserve">/* См. также: MediaWiki:Common.js */

// Для альтернативных версий текста

$(function(){
	// Другие редакции
	if ($(&quot;#altEditions&quot;).length) {
		$(&quot;#altEditions&quot;)
			.insertBefore( $(&quot;#p-coll-print_export&quot;) )
			.wrap( &quot;&lt;div class='portlet' id='p-editions'&gt;&lt;/div&gt;&quot; )
			.before( &quot;&lt;h3 id='p-editions-label'&gt;Другие редакции&lt;/h3&gt;&quot; )
			.addClass( &quot;pBody&quot; ).css( &quot;display&quot;, &quot;&quot; );
		$(&quot;#altEditions li&quot;).has(&quot;.selflink&quot;).remove();
		$(&quot;#altEditions li&quot;).has(&quot;a[href^='http']&quot;).remove();
		$(&quot;#altEditions a.new&quot;).css( &quot;color&quot;, &quot;#ba0000&quot; );
	}
	
	// Другие версии
	if ($(&quot;#otherVersions&quot;).length) {
		$(&quot;#otherVersions&quot;)
			.insertBefore( $(&quot;#p-coll-print_export&quot;) )
			.wrap( &quot;&lt;div class='portlet' id='p-versions'&gt;&lt;/div&gt;&quot; )
			.before( &quot;&lt;h3 id='p-versions-label'&gt;Другие версии&lt;/h3&gt;&quot; )
			.addClass( &quot;pBody&quot; ).css( &quot;display&quot;, &quot;&quot; );
		$(&quot;#otherVersions a.new&quot;).css( &quot;color&quot;, &quot;#ba0000&quot; );
	}
	
	// В других проектах
	if ($(&quot;#otherProjects&quot;).length) {
		$(&quot;#otherProjects&quot;)
			.insertBefore( $(&quot;#p-coll-print_export&quot;) )
			.wrap( &quot;&lt;div class='portlet' id='p-projects'&gt;&lt;/div&gt;&quot; )
			.before( &quot;&lt;h3 id='p-projects-label'&gt;В других проектах&lt;/h3&gt;&quot; )
			.addClass( &quot;pBody&quot; ).css( &quot;display&quot;, &quot;&quot; );
		$(&quot;#otherProjects a.new&quot;).css( &quot;color&quot;, &quot;#ba0000&quot; );
	}
});</text>
      <sha1>1c5jywet59ttlf7aam24t6dohtuafaj</sha1>
    </revision>
  </page>
  <page>
    <title>MediaWiki:Edittools</title>
    <ns>8</ns>
    <id>141</id>
    <revision>
      <id>3141168</id>
      <parentid>3137840</parentid>
      <timestamp>2018-02-26T18:47:20Z</timestamp>
      <contributor>
        <username>Sergey kudryavtsev</username>
        <id>265</id>
      </contributor>
      <comment>+ РБС/Ссылка</comment>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve">&lt;div id=&quot;editpage-specialchars&quot; style=&quot;margin-top:1px;border:1px solid #aaa;padding:2px&quot;&gt;
&lt;span style=&quot;border-bottom:1px dotted gray; cursor:help&quot; title=&quot;Эти ссылки служат для быстрой вставки разметки в окно редактирования&quot;&gt;&lt;small&gt;Быстрая вставка&lt;/small&gt;&lt;/span&gt;:
&lt;span style=&quot;font-size:1.3em&quot;&gt;&lt;charinsert&gt; «+» „+“ — … | «+…»&lt;/charinsert&gt;&lt;/span&gt;
&lt;charinsert&gt;&amp;#123;{+}} [[+]] [[|+]] &lt;nowiki&gt;&lt;br /&gt;&lt;/nowiki&gt; &lt;nowiki&gt;&amp;amp;nbsp;&lt;/nowiki&gt; &lt;nowiki&gt;&amp;amp;thinsp;&lt;/nowiki&gt;&lt;/charinsert&gt;
&lt;small&gt;
&amp;nbsp;&lt;charinsert&gt;[[../|+]] [[w:|+]] {{ЭСБЕ/Автор|+}} {{РБС/Автор|+}} {{ЭСБЕ/Ссылка|+}} {{РБС/Ссылка|+}} {{ping|+}}&lt;/charinsert&gt;

'''Заголовки и сноски:'''
&lt;charinsert&gt;&lt;nowiki&gt;== + ==&lt;/nowiki&gt;&lt;/charinsert&gt; &amp;nbsp; &lt;charinsert&gt;&lt;nowiki&gt;=== + ===&lt;/nowiki&gt;&lt;/charinsert&gt; &amp;nbsp; &lt;charinsert&gt;&lt;nowiki&gt;== См. также ==&lt;/nowiki&gt;&lt;/charinsert&gt; &amp;nbsp; &lt;charinsert&gt;&lt;nowiki&gt;== Ссылки ==&lt;/nowiki&gt;&lt;/charinsert&gt; · 
&lt;charinsert&gt;&lt;nowiki&gt;&lt;ref&gt;&lt;/nowiki&gt;+&lt;nowiki&gt;&lt;/ref&gt;&lt;/nowiki&gt; &lt;nowiki&gt;&lt;ref name=&quot;&quot;&gt;&lt;/nowiki&gt;+&lt;nowiki&gt;&lt;/ref&gt;&lt;/nowiki&gt; &lt;nowiki&gt;&lt;ref name=&quot;&quot; /&gt;&lt;/nowiki&gt; &lt;nowiki&gt;&lt;ref follow=&quot;&quot;&gt;+&lt;/ref&gt;&lt;/nowiki&gt; &lt;nowiki&gt;== Примечания ==&amp;#10;&amp;#123;{примечания}}&lt;/nowiki&gt; {{примечания|title=}}&lt;/charinsert&gt;

'''HTML теги:'''
&lt;charinsert&gt;&lt;&gt;+&lt;/&gt; &lt;nowiki&gt;&lt;!-- +--&gt;&lt;/nowiki&gt; &lt;u&gt;+&lt;/u&gt; &lt;s&gt;+&lt;/s&gt; &lt;center&gt;+&lt;/center&gt; &lt;small&gt;+&lt;/small&gt; &lt;big&gt;+&lt;/big&gt; &lt;sub&gt;+&lt;/sub&gt; &lt;sup&gt;+&lt;/sup&gt; &lt;blockquote&gt;+&lt;/blockquote&gt; &lt;tt&gt;+&lt;/tt&gt; &lt;pre&gt;+&lt;/pre&gt; &lt;code&gt;+&lt;/code&gt; &lt;code&gt;&amp;lt;nowiki&gt;+&lt;/nowiki&gt;&lt;/code&gt; &lt;/charinsert&gt; 

'''Расширения:'''
&lt;charinsert&gt;&lt;poem&gt;+&lt;/poem&gt; &lt;math&gt;+&lt;/math&gt; &lt;gallery&gt;+&lt;/gallery&gt; &lt;nowiki&gt;&lt;source lang=&quot;&quot;&gt;&lt;/nowiki&gt;+&lt;/source&gt; &lt;nowiki&gt;&lt;section begin=&quot;&quot;/&gt;+&lt;section end=&quot;&quot;/&gt;&lt;/nowiki&gt;&lt;/charinsert&gt; &amp;nbsp;

'''Служебные:'''
&lt;charinsert&gt;&lt;nowiki&gt;#перенаправление [[&lt;/nowiki&gt;+]]&lt;/charinsert&gt;&amp;nbsp;
&lt;charinsert&gt;[[Категория:+]] {{КЛЮЧ_СОРТИРОВКИ:+}}&lt;/charinsert&gt;&amp;nbsp;
&lt;charinsert&gt;__NOTOC__ __TOC__ __FORCETOC__ __NOEDITSECTION__ &lt;/charinsert&gt;
&lt;charinsert&gt;&amp;lt;nowiki&gt;+&lt;/nowiki&gt; &lt;includeonly&gt;+&lt;/includeonly&gt; &lt;noinclude&gt;+&lt;/noinclude&gt;&lt;/charinsert&gt;

&lt;/small&gt;

&lt;small&gt;'''Символы:'''&lt;/small&gt;
&lt;charinsert&gt;‘ “ ’ ” ~ # @ § ¶ № • · ← ↖ ↑ ↗ → ↘ ↓ ↙ ↔ ⇄ ↕ ¡ ¿ \ ½ ⅓ ⅔ ¼ ¾ ⅕ ⅖ ⅗ ⅘ ⅙ ⅚ ⅛ ⅜ ⅝ ⅞ ≈ ≠ ± − × ÷ ° ^ ¹ ² ³ € £ ¥ $ ¢ © ® ™ †&lt;/charinsert&gt;
&lt;span title=&quot;Знак ударения, ставится после ударной гласной&quot;&gt;&lt;charinsert&gt; &amp;#123;{подст:ударение}}&lt;/charinsert&gt;&lt;/span&gt;

&lt;small&gt;'''Греческий алфавит:'''&lt;/small&gt;
&lt;span style=&quot;font-size:120%&quot;&gt;
&lt;charinsert&gt; Α α Β β Γ γ Δ δ &lt;/charinsert&gt; &amp;nbsp;
&lt;charinsert&gt; Ε ε Ζ ζ Η η Θ θ &lt;/charinsert&gt; &amp;nbsp;
&lt;charinsert&gt; Ι ι Κ κ Λ λ Μ μ &lt;/charinsert&gt; &amp;nbsp;
&lt;charinsert&gt; Ν ν Ξ ξ Ο ο Π π &lt;/charinsert&gt; &amp;nbsp;
&lt;charinsert&gt; Ρ ρ Σ σ ς Τ τ Υ υ &lt;/charinsert&gt; &amp;nbsp;
&lt;charinsert&gt; Φ φ Χ χ Ψ ψ Ω ω &lt;/charinsert&gt; &amp;nbsp;
&lt;/span&gt;

&lt;small&gt;'''Кириллица:'''&lt;/small&gt;
&lt;span style=&quot;font-family:'Arial Unicode MS',Cambria,Consolas,'Microsoft Sans Serif','DejaVu Sans',FreeSerif,'Palatino Linotype';font-size:120%&quot;&gt;
&lt;charinsert&gt; І і Ѣ ѣ Ѳ ѳ Ѵ ѵ — &lt;/charinsert&gt; &amp;nbsp;
&lt;charinsert&gt; Ё ё Ѱ ѱ ѱ҃ Ѯ ѯ ѯ҃ &lt;/charinsert&gt; &amp;nbsp;
&lt;charinsert&gt; Ѫ ѫ Ѭ ѭ Ѧ ѧ Ѩ ѩ &lt;/charinsert&gt; &amp;nbsp;
&lt;charinsert&gt; Ѻ ѻ҃ Ѡ ѡ Ѿ ѿ  &lt;/charinsert&gt; &amp;nbsp;
&lt;charinsert&gt; Ї ї Є є Ѥ ѥ Ѹ ѹ Ѕ ѕ ıа &lt;/charinsert&gt; &amp;nbsp;
&lt;charinsert&gt; ҂ &lt;/charinsert&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;
&lt;charinsert&gt;  ҃ &lt;/charinsert&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;
&lt;charinsert&gt;  ҄ &lt;/charinsert&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;
&lt;charinsert&gt;  ҅ &lt;/charinsert&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;
&lt;charinsert&gt;  ҆ &lt;/charinsert&gt; &amp;nbsp;&lt;/span&gt;

&lt;small&gt;'''Латиница:'''&lt;/small&gt;
&lt;charinsert&gt; Á á Ä ä Å å È è É é Ê ê Ì ì Í í Ò ò Ó ó Ö ö Ú ú Ü ü Ç ç ſ &lt;/charinsert&gt;
&lt;/div&gt;</text>
      <sha1>3mwn9ex8pefwakdxn5o94jgizbf9hy5</sha1>
    </revision>
  </page>
  <page>
    <title>MediaWiki:Linkprefix</title>
    <ns>8</ns>
    <id>619</id>
    <revision>
      <id>3579</id>
      <parentid>1444</parentid>
      <timestamp>2005-09-12T14:54:16Z</timestamp>
      <contributor>
        <username>Александр Сигачёв</username>
        <id>4</id>
      </contributor>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve">/^(.*?)(„|«)$/sD</text>
      <sha1>32r1t1ke0ulgdrf7rxfuir75jyqkegx</sha1>
    </revision>
  </page>
  <page>
    <title>MediaWiki:Linktrail</title>
    <ns>8</ns>
    <id>622</id>
    <revision>
      <id>3578</id>
      <parentid>1441</parentid>
      <timestamp>2005-09-12T14:53:52Z</timestamp>
      <contributor>
        <username>Александр Сигачёв</username>
        <id>4</id>
      </contributor>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve">/^((?:[a-z]|а|б|в|г|д|е|ё|ж|з|и|й|к|л|м|н|о|п|р|с|т|у|ф|х|ц|ч|ш|щ|ъ|ы|ь|э|ю|я|“|»)+)(.*)$/sD</text>
      <sha1>1tmveucgiaovre3roi04nd0r6qr65i4</sha1>
    </revision>
  </page>
  <page>
    <title>MediaWiki:Listingcontinuesabbrev</title>
    <ns>8</ns>
    <id>624</id>
    <revision>
      <id>6977</id>
      <parentid>624</parentid>
      <timestamp>2005-12-15T17:44:27Z</timestamp>
      <contributor>
        <username>Александр Сигачёв</username>
        <id>4</id>
      </contributor>
      <minor />
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve"> (продолжение)</text>
      <sha1>ihme40iqmm3htkjaicyrc259zr2h0vc</sha1>
    </revision>
  </page>
  <page>
    <title>MediaWiki:Newwindow</title>
    <ns>8</ns>
    <id>752</id>
    <revision>
      <id>10216</id>
      <parentid>752</parentid>
      <timestamp>2006-03-25T22:55:10Z</timestamp>
      <contributor>
        <username>Александр Сигачёв</username>
        <id>4</id>
      </contributor>
      <minor />
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve" />
      <sha1>phoiac9h4m842xq45sp7s6u21eteeq1</sha1>
    </revision>
  </page>
  <page>
    <title>MediaWiki:Prefixindex</title>
    <ns>8</ns>
    <id>847</id>
    <revision>
      <id>1301</id>
      <parentid>847</parentid>
      <timestamp>2005-08-29T06:19:28Z</timestamp>
      <contributor>
        <username>Александр Сигачёв</username>
        <id>4</id>
      </contributor>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve">Указатель по началу слов</text>
      <sha1>ckqcej6uon8355bzvbmqxpq57fv0wkq</sha1>
    </revision>
  </page>
  <page>
    <title>MediaWiki:Shareduploadwiki</title>
    <ns>8</ns>
    <id>982</id>
    <revision>
      <id>3580</id>
      <parentid>1303</parentid>
      <timestamp>2005-09-12T14:56:00Z</timestamp>
      <contributor>
        <username>Александр Сигачёв</username>
        <id>4</id>
      </contributor>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve">Дополнительную информацию можно найти на $1.</text>
      <sha1>g6mvfm3abuyymde9sw1e55xfdzp70eh</sha1>
    </revision>
  </page>
  <page>
    <title>MediaWiki:Showhidebots</title>
    <ns>8</ns>
    <id>988</id>
    <revision>
      <id>3581</id>
      <parentid>1304</parentid>
      <timestamp>2005-09-12T14:56:30Z</timestamp>
      <contributor>
        <username>Александр Сигачёв</username>
        <id>4</id>
      </contributor>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve">($1 ботов)</text>
      <sha1>iw3qdvyyboe3s7wmn40eejwdn3pytgm</sha1>
    </revision>
  </page>
  <page>
    <title>MediaWiki:Sidebar</title>
    <ns>8</ns>
    <id>995</id>
    <revision>
      <id>183424</id>
      <parentid>180131</parentid>
      <timestamp>2009-06-04T02:11:22Z</timestamp>
      <contributor>
        <username>Innv</username>
        <id>938</id>
      </contributor>
      <minor />
      <comment>унификация</comment>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve">* SEARCH
* navigation
** mainpage|mainpage
** randompage-url|randompage
** recentchanges-url|recentchanges
** statistics-url|statistics
** newpages-url|newpages

* participation
** forum-url|forum
** news-url|news
** announce-url|announce
** literature-url|literature
** tribune-url|tribune
** helppage|help
** donate-url|donate
* TOOLBOX</text>
      <sha1>ohn7m5vbsbu2ps670z4rjoaslly0pbs</sha1>
    </revision>
  </page>
  <page>
    <title>MediaWiki:Sitenotice</title>
    <ns>8</ns>
    <id>997</id>
    <revision>
      <id>2244113</id>
      <parentid>2242841</parentid>
      <timestamp>2016-03-26T22:36:18Z</timestamp>
      <contributor>
        <username>Hinote</username>
        <id>25052</id>
      </contributor>
      <comment>clear</comment>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve" />
      <sha1>phoiac9h4m842xq45sp7s6u21eteeq1</sha1>
    </revision>
  </page>
  <page>
    <title>MediaWiki:Tagline</title>
    <ns>8</ns>
    <id>1035</id>
    <revision>
      <id>4420</id>
      <parentid>1035</parentid>
      <timestamp>2005-09-18T20:39:14Z</timestamp>
      <contributor>
        <username>Александр Сигачёв</username>
        <id>4</id>
      </contributor>
      <comment>Материал из Викитеки — свободной библиотеки</comment>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve">Материал из Викитеки — свободной библиотеки</text>
      <sha1>4quv1seezz42xn47enhm060341hh9f0</sha1>
    </revision>
  </page>
  <page>
    <title>Заглавная страница</title>
    <ns>0</ns>
    <id>1290</id>
    <revision>
      <id>2821455</id>
      <parentid>2821349</parentid>
      <timestamp>2017-10-12T22:28:17Z</timestamp>
      <contributor>
        <username>Lozman</username>
        <id>607</id>
      </contributor>
      <minor />
      <comment>Изменил уровень защиты [[Заглавная страница]]: популярная страница ([Редактирование=Разрешено только администраторам] (бессрочно) [Переим…</comment>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve">__NOTOC__ __NOEDITSECTION__
{| width=&quot;100%&quot; cellpadding=&quot;0&quot; cellspacing=0 border=0
|-
| colspan=&quot;2&quot; width=&quot;100%&quot; style=&quot;vertical-align:top; padding-right:0px;&quot; |
{{Шапка}}
|-
| width=&quot;50%&quot; style=&quot;vertical-align:top; padding-right:4px;&quot; |
{{/box|#C8D8FF|{{Анонсы на сегодня}}}}
| width=&quot;50%&quot; style=&quot;vertical-align:top; padding-left:4px;&quot; |
{{/box|#C8D8FF|{{Новости сайта}}}}
{{/box|#C8D8FF|{{Оглавление}}}}
{{/box|#C8D8FF|{{Объявления}}}}
|-
| colspan=&quot;2&quot; width=&quot;100%&quot; style=&quot;vertical-align:top; padding-right:0px;&quot; |
{{/box|#C8D8FF|{{Сообщество фонда Викимедиа}}}}
|}
&lt;div style=&quot;text-align:center;font-size:83%&quot;&gt;&lt;span class=&quot;plainlinks&quot;&gt;[http://ru.m.wikisource.org/wiki/Заглавная_страница Мобильная версия]&lt;/span&gt; — [[wmf:Заглавная страница|Фонд Викимедиа]] — [[m:Wikisource/Table|Другие языковые разделы]] &lt;/div&gt;</text>
      <sha1>0tef0hp11j2s1zxc6bgxem6zlembt55</sha1>
    </revision>
  </page>
  <page>
    <title>Участник:ChVA</title>
    <ns>2</ns>
    <id>1291</id>
    <revision>
      <id>2525556</id>
      <parentid>963780</parentid>
      <timestamp>2017-05-18T19:02:34Z</timestamp>
      <contributor>
        <username>Ratte</username>
        <id>43696</id>
      </contributor>
      <minor />
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve">__NOTOC__

Виталий Чихарин. Администратор (а также «бюрократ») русскоязычного раздела Викитеки.

см. также [http://www.livejournal.com/users/chva/ мой ЖЖ]

Пишу некоторые статьи для Википедии ([[w:ru:Участник:ChVA|ChVA]]).

* [[Special:Contributions/ChVA|Что сделано]] — системная страница
* [http://toolserver.org/~soxred93/pcount/index.php?name=ChVA&amp;lang=ru&amp;wiki=wikisource График моей активности]

== Инструменты ==

* [[Служебная:NewPages|Патрулирование статей]]
* [http://ru.wikisource.org/w/index.php?title=Служебная:NewPages&amp;hidepatrolled=1 То же, но только непроверенные статьи]
* [http://ru.wikisource.org/wiki/MediaWiki:Titleblacklist Список запрещённых &lt;s&gt;книг&lt;/s&gt; названий]
* [[Служебная:ValidationStatistics|Статистика патрулирования]]

== Полезные шаблоны ==

* [[Викитека:Список общих шаблонов, полезных для редактирования|Список общих шаблонов, полезных для редактирования]]
* [[Викитека:Шаблоны источников информации|Список шаблонов источников информации]]

== Полезные служебные статьи ==

* [[Викитека:Электронные_библиотеки|Список электронных библиотек]]

== Мой бот ==

В Викитеке работает мой бот, его зовут [[Участник:ChVABOT|ChVABOT]], [[Участник:ChVABOT/Что сделано|вот список выполненных им заданий]] (список по всем выполненным заданиям больше не веду, только по самым крупным).

== To Do ==

# Добавить недостающие статьи в [[Сборник боевых документов]] {{Сделано}}
# Разобраться с current, next и prev при использовании команды &lt;nowiki&gt;&lt;pages/&gt;&lt;/nowiki&gt; + внести соответствующие изменения на страницу [[Викитека:Проект:OCR|Проекта OCR]] {{Сделано}}.
# Изменить страницу индекса для русской Викитеки по примеру английской и французской (больше полей, выпадающие списки) {{Сделано}}
# Разобраться с [[oldwikisource:Wikisource:Shared Scripts|дополнительными скрпитами для Proofread]]
# Переделать [[Индекс:Анна Каренина part 1-4.pdf|1-й том Анны Карениной]] под &lt;nowiki&gt;&lt;pages/&gt;&lt;/nowiki&gt; {{Сделано}}
# Внести в Викитеку [[Индекс:Дешевая юмористическая библиотека Нового Сатирикона, Выпуск 23.djvu|23-й сборник Аверченко из дешёвой библиотеки Нового Сатирикона]] ([http://dlib.rsl.ru/download.php?path=/rsl01004000000/rsl01004464000/rsl01004464335/rsl01004464335.pdf&amp;size= на сайте РГБ]). {{Сделано}}
# Переделать [[Как постепенно дошли люди до настоящей арифметики]] (''отложил'' пока не получу доступ к планшетному сканеру)
# Проверить непроверенные страницы, начинающиеся на букву А {{Сделано}}
# Проверить стихотворения Марины Цветаевой {{Сделано}}
# Составить справку по оформлению драматических произведений {{Сделано}}
# Проверить непроверенные страницы, начинающиеся на букву Б
# Перенести в Викитеку все произведения [[Александр Петрович Сумароков|Сумарокова]] с [http://rvb.ru/18vek/sumarokov/toc.htm этой] страницы {{Сделано}}
# Полностью переработать все Стихотворения в прозе [[Стихотворения в прозе (Тургенев)|Тургенева]] {{Сделано}}
# Сделать [[Индекс:Sbornik zakonov 1938-1956.djvu|Сборник Законов СССР и Указов Президиума Верховного Совета (1938 — 1956)]] {{Сделано}} (совместно)
# Разобраться с ГОСТами {{Сделано}}
# [[Указ Президиума ВС СССР от 10.11.1945 о выходе из советского гражданства лиц польской и еврейской национальностей, бывших польских граждан ...]], [[Постановление СНК СССР от 28.07.1941 № 1902]] — ссылки

== Другое ==

* [[Викитека:Проект:OCR|Проект OCR]]
* [http://ru.wikisource.org/w/api.php?action=query&amp;meta=siteinfo&amp;siprop=namespaces Номера пространств в Викитеке]
* [[/Шпаргалка по тэгу HR|Шпаргалка по тэгу HR]]
* [[/Правильное оформление первого абзаца для страниц индексов, которые будут потом включаться в основное пространство командой pages|Правильное оформление первого абзаца для страниц индексов, которые будут потом включаться в основное пространство командой pages]]

Недокументированный параметр &lt;nowiki&gt;&lt;math&gt;&lt;/nowiki&gt;:

&lt;pre&gt;&lt;math&gt;\Gamma(z) =\int_0^\infty e^{-t} t^{z-1} \,dt\,&lt;/math&gt; using scriptstyle tag is rendered:  &lt;math&gt;\scriptstyle\Gamma(z) =\scriptstyle \int_0^\infty e^{-t} t^{z-1} \,dt\,&lt;/math&gt;&lt;/pre&gt;

&lt;math&gt;\Gamma(z) =\int_0^\infty e^{-t} t^{z-1} \,dt\,&lt;/math&gt; using scriptstyle tag is rendered:  &lt;math&gt;\scriptstyle\Gamma(z) =\scriptstyle \int_0^\infty e^{-t} t^{z-1} \,dt\,&lt;/math&gt;</text>
      <sha1>6b3g096yuibn0ar7wqq5hcpqxziff2p</sha1>
    </revision>
  </page>
  <page>
    <title>Участник:Guria</title>
    <ns>2</ns>
    <id>1294</id>
    <revision>
      <id>1296</id>
      <timestamp>2005-08-28T04:40:26Z</timestamp>
      <contributor>
        <username>Guria</username>
        <id>3</id>
      </contributor>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve">{| style=&quot;float: right; margin-left: 1em; margin-bottom: 0.5em; width: 242px; border: #99B3FF solid 1px; text-align: center&quot;
|+ '''[[Википедия:Вавилон]]'''
|-
| {{User ru}}
|-
| {{User en-2}}
|}
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
{| style=&quot;float: right; margin-left: 1em; margin-bottom: 0.5em; width: 242px; border: #99B3FF solid 1px; text-align: center&quot;
|+On others wikis
|[[:w:ru:Участник:Guria|Ru Guria]]
|-
|[[:m:User:Guria|Meta Guria]]
|-
|[[:w:en:User:GuriaRus|En GuriaRus]]
|}</text>
      <sha1>25zmdvv5lam3xc3iwg8mkem3u5x5t1t</sha1>
    </revision>
  </page>
  <page>
    <title>Участник:Александр Сигачёв</title>
    <ns>2</ns>
    <id>1295</id>
    <revision>
      <id>916650</id>
      <parentid>582532</parentid>
      <timestamp>2012-10-07T12:29:03Z</timestamp>
      <contributor>
        <username>Lozman</username>
        <id>607</id>
      </contributor>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve">'''Александр Сигачёв''', бывший администратор (и «бюрократ») Викитеки.

Подробнее обо мне можно уздать на [[w:ru:Участник:Александр Сигачёв|моей странице в Википедии]].

See also:
*[[meta:User:.:Ajvol:.]]</text>
      <sha1>qu921dbgsou6m61x32xoii1r7bzy35h</sha1>
    </revision>
  </page>
  <page>
    <title>Участник:Monedula</title>
    <ns>2</ns>
    <id>1296</id>
    <revision>
      <id>291247</id>
      <parentid>291197</parentid>
      <timestamp>2009-10-01T12:22:46Z</timestamp>
      <contributor>
        <username>Sergey kudryavtsev</username>
        <id>265</id>
      </contributor>
      <comment>rv: спам</comment>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve">{{Участник Википедии}}</text>
      <sha1>5a86l0epkrtlkwpiw9p541gh60dbxkx</sha1>
    </revision>
  </page>
  <page>
    <title>MediaWiki:Forum</title>
    <ns>8</ns>
    <id>1297</id>
    <revision>
      <id>1307</id>
      <timestamp>2005-08-29T06:24:58Z</timestamp>
      <contributor>
        <username>Александр Сигачёв</username>
        <id>4</id>
      </contributor>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve">Форум</text>
      <sha1>tnza9bxueq0ser4pmr4sijy74m1movm</sha1>
    </revision>
  </page>
  <page>
    <title>MediaWiki:Forum-url</title>
    <ns>8</ns>
    <id>1299</id>
    <revision>
      <id>1309</id>
      <timestamp>2005-08-29T06:33:31Z</timestamp>
      <contributor>
        <username>Александр Сигачёв</username>
        <id>4</id>
      </contributor>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve">{{ns:project}}:Форум</text>
      <sha1>rbbqfz73veqtjd6u38xyxl05e65emy1</sha1>
    </revision>
  </page>
  <page>
    <title>Викитека:Описание</title>
    <ns>4</ns>
    <id>1301</id>
    <redirect title="Справка:Что такое Викитека?" />
    <revision>
      <id>461683</id>
      <parentid>97392</parentid>
      <timestamp>2011-01-13T10:06:00Z</timestamp>
      <contributor>
        <username>ChVA</username>
        <id>2</id>
      </contributor>
      <comment>Перенаправление на [[Справка:Что такое Викитека?]]</comment>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve">#REDIRECT [[Справка:Что такое Викитека?]]</text>
      <sha1>g163hdllf025a8x6ibrwkvggtz26wox</sha1>
    </revision>
  </page>
  <page>
    <title>Викитека:Отказ от ответственности</title>
    <ns>4</ns>
    <id>1302</id>
    <revision>
      <id>212970</id>
      <parentid>212965</parentid>
      <timestamp>2009-08-06T12:56:03Z</timestamp>
      <contributor>
        <username>Infovarius</username>
        <id>158</id>
      </contributor>
      <minor />
      <comment>добавлена категория «Викитека:Справка» с помощью [[ВТ:HOTCAT|HotCat]]</comment>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve">См. аналогичную статью в [[w:ru:Википедия:Отказ от ответственности|Википедия:Отказ от ответственности]]

[[Категория:Викитека:Мягкие перенаправления]]

[[Категория:Викитека:Справка]]</text>
      <sha1>lqhnowx86kmy26fy3cq4ylp7uqrkji3</sha1>
    </revision>
  </page>  
</mediawiki>
"""

# Путь к файлу wikidump
PATHTOXML = '/home/vladislav/var/wikidumps/ruwikisource-20180301-pages-meta-current.xml'
# PATHTOXML = '/home/vladislav/var/dal/Викитека-20180409165247.xml'


def parseBookXML(xmlFile):
    # with open(xmlFile) as fobj:
    # 	xml = fobj.read()
    xml = txt
    root = etree.fromstring(xml)
    # root = etree.parse('path_to_file')

    from xml.etree import ElementTree as EET

    parser = etree.XMLParser(ns_clean=True)
    tree = etree.parse(StringIO(xml), parser)

    from xml.etree import ElementTree

    # namespaces
    NS_MAIN = 2
    NS_PAGE = 104

    book_dict = {}
    books = []
    for book in root.getchildren():
        for elem in book.getchildren():
            if elem.tag != 'page': continue  # work only on pages
            if int(elem.ns) not in [NS_PAGE]: continue
            if not elem.text:
                text = "None"
            else:
                text = elem.text
            print(elem.tag + " => " + text)
            book_dict[elem.tag] = text

            if book.tag == "book":
                books.append(book_dict)
                book_dict = {}

    return books


# out = open("/tmp/output.txt", "w", encoding="utf-8")


import re
from pywikibot import output, xmlreader
from urllib.parse import urlparse, parse_qs, parse_qsl, unquote, quote

wikilink_re1 = re.compile(r"\[\[РСКД/([^]|]+)")
wikilink_re2 = re.compile(r"\[\[../([^]|]+)")
wikilink_re3 = re.compile(r"\{[\{([wW]l\|([^}|]+)")
redirect_target_re = re.compile(r"#перенаправление \[\[([^]]+)")

all_found_titles = []
titles_and_links = []
redirects = []


def main():
    dump = xmlreader.XmlDump(PATHTOXML)
    # readPagesCount = 0
    for entry in dump.parse():
        if int(entry.ns) not in [0] \
                or not entry.title.startswith('РСКД/') \
                or 'РСКД/Словник' in entry.title \
                or 'РСКД/Русский указатель статей' == entry.title \
                or 'РСКД/Список сокращений названий трудов античных авторов' == entry.title:
            continue
        if entry.isredirect:
            redirects.append(dict(t=entry.title, r=redirect_target_re.search(entry.text).group(1)))

        if 'РСКД/Цезарь' in entry.title:
            print(entry.title)
        all_found_titles.append(entry.title)

        links = []
        links.extend(wikilink_re1.findall(entry.text))
        links.extend(wikilink_re2.findall(entry.text))
        links.extend(wikilink_re3.findall(entry.text))
        links = [f'РСКД/{l}' for l in links]
        if links:
            print({'t': entry.title, 're': links})
            titles_and_links.append({'t': entry.title, 're': links})

        # readPagesCount += 1
        # if readPagesCount % 10000 == 0:
        #     output("%i pages read..." % readPagesCount)

    pass
    # a = [links['re'] for links in titles_and_links]
    # all_links = {l for ls in a for l in ls}
    all_links = {l.rsplit('#')[0] for links in titles_and_links for l in links['re']}
    error_links = {l for l in all_links if l not in all_found_titles}
    # ltxt = '\n'.join([f'# [[{e}]]' for e in error_links])
    ltxt = '\n'.join([f'# [[{e}]] - [[Служебная:Ссылки сюда/{quote(e)}|ссылки сюда]]' for e in error_links])
    pass

    # ссылки у которых есть похожие названия страниц с окончаниями (вроде "РСКД/Корон" и "РСКД/Корона"). для поиска ошибочных ссылок\
    # [[s:ru:Обсуждение:Реальный словарь классических древностей#Викиссылки]]
    links_and_likes_titles = [(l, t) for l in all_links for t in all_found_titles if t.startswith(l) and t != l]
    # только в редиректах
    g = [(l, r['t']) for l in all_links for r in redirects if r['t'].startswith(l) and r['t'] != l]

    # find_entry =  [i['t'] for i in titles_and_links if 'РСКД/Ilya' in i['re']]

    # remove entry in dict by found value
    # [titles_and_links.remove(i) for i in titles_and_links if i['t'] == 'РСКД/Русский указатель статей']
    pass


if __name__ == "__main__":
    # parseBookXML(xml_path_wikidump)
    # pass
    main()
