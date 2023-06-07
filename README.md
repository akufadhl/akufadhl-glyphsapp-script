# akufadhl-glyphs-script
Collections of Glyphsapp Script

## Contextual Kerning
A collection of scripts to calculate and avoid below shape collisions in **Javanese**, **Balinese**, and **Kawi** scripts. You can try the script with this font [Tuladha Jejeg OT](https://github.com/akufadhl/Tuladha-Jejeg-OT)

NOTE: *Works best for a single master file, Glyphsapp don't support Number Values interpolation yet. and it also genereate GPOS error with Fontmake. USE WISELY*
  - **Calculate Kern Feature**

    Loop through Base consonants, and mark/conjuncts (below shapes). If below shapes is wider than consonant, the remaining space is added +threshold. Groups/classes is generated and added to the feature tab
    ![Calculate Kern Image](./CalculateKern.png)
  - **Preview Kerning List**
  
    Preview pre-generated kerning lists.
    ![Calculate Kern Image](./KernPreview.png)
