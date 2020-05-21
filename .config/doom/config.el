;; Set transparency
; https://emacs.stackexchange.com/questions/5944/is-there-a-transparent-theme
(set-frame-parameter (selected-frame) 'alpha '(90 90))
(add-to-list 'default-frame-alist '(alpha 90 90))

;; Font size change
(setq doom-font (font-spec :family "monospace" :size 15))

;; Theme selection
(setq doom-theme 'doom-dracula)

;; Show lines and columns
(setq display-line-numbers-type t)

;; Show trailing whitespace
(setq-default show-trailing-whitespace t)

;;;;;;;;; ORG MODE COMMANDS ;;;;;;;;;
(setq org-directory "~/org/")
