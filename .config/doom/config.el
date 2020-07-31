;; Font size change
(setq doom-font (font-spec :family "monospace" :size 15))

;; Theme selection
(setq doom-theme 'doom-dracula)

;; Show lines and columns
(setq display-line-numbers t)

;; Show trailing whitespace
(setq-default show-trailing-whitespace t)

;;;;;;;;; MODES ;;;;;;;;;
;; Spell check
(add-hook 'text-mode-hook 'flyspell-mode)
(add-hook 'prog-mode-hook 'flyspell-prog-mode)

;; Math mode
; https://www.gnu.org/software/auctex/manual/auctex/Mathematics.html
(add-hook 'LaTeX-mode-hook 'LaTeX-math-mode)

;; Reftex mode
; https://tex.stackexchange.com/questions/36876/reftex-doesnt-turn-on-automatically-when-loading-auctex-after-upgrade-to-tex-li
(add-hook 'LaTeX-mode-hook 'turn-on-reftex)
(setq reftex-plug-into-AUCTeX t)

;; Inline images notebook
; https://github.com/hlissner/doom-emacs/issues/2545
(setq ein:output-area-inlined-images t)
