# Make lexicon.fst

http://openfst.org/twiki/bin/view/FST/FstExamples

## Tokenization, charaters to word 
$ fstcompile --isymbols=ascii.syms --osymbols=wotw.syms >Mars.fst <<EOF
0 1 M Mars
1 2 a <epsilon>
2 3 r <epsilon>
3 4 s <epsilon>
4
EOF

## draw
$ fstdraw --isymbols=ascii.syms --osymbols=wotw.syms -portrait Mars.fst | dot -Tjpg >Mars.jpg

## make lexicon 
$ fstunion man.fst Mars.fst | fstunion - Martian.fst | fstclosure >lexicon.fst

fstclosure 后 17 个节点。

## optimize lexicon size
$ fstrmepsilon lexicon.fst | fstdeterminize | fstminimize >lexicon_opt.fst

fstrmepsilon 后 15 个节点

fstdterminize 后 11 个节点

fstminimize 后 6 个节点 

## handle punctuation symbols

$ fstcompile --isymbols=ascii.syms --osymbols=wotw.syms >punct.fst <<EOF
0 1 <space> <epsilon>
0 1 . <epsilon>
0 1 , <epsilon>
0 1 ? <epsilon>
0 1 ! <epsilon>
1
EOF

$ fstunion man.fst Mars.fst | fstunion - Martian.fst | fstconcat - punct.fst | fstclosure >lexicon.fst

fstconcat 后 18 个节点, 之前是 17 个节点。




