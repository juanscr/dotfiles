;;;;;;;;;;;;;;;;;;;;; MODES ;;;;;;;;;;;;;;;;;;;;;;;
;; Agda mode
(load-file (let ((coding-system-for-read 'utf-8))
	     (shell-command-to-string "agda-mode locate")))

;; Spell check
(add-hook 'text-mode-hook 'flyspell-mode)
(add-hook 'prog-mode-hook 'flyspell-prog-mode)

;;;;;;;;;;;;;;;;;;;;; EDITOR ;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;; STYLE ;;;;;;;
;; Set transparency
; https://emacs.stackexchange.com/questions/5944/is-there-a-transparent-theme
(set-frame-parameter (selected-frame) 'alpha '(80 80))
(add-to-list 'default-frame-alist '(alpha 80 80))

;; Trailing Whitespace
(setq-default show-trailing-whitespace t)

;; Line Number
(setq-default display-line-numbers t)

;; Column number
(setq column-number-mode t)

;; Hide tool bar
; https://superuser.com/questions/127420/how-can-i-hide-the-tool-bar-in-emacs-persistently
(tool-bar-mode -1)

;; Hide Scroll bar
; https://www.emacswiki.org/emacs/ScrollBar
(scroll-bar-mode -1)

;; Hide menu bar
; https://stackoverflow.com/questions/53958292/remove-the-emacs-menu-bar
(menu-bar-mode -1)

;; Math mode
; https://www.gnu.org/software/auctex/manual/auctex/Mathematics.html
(add-hook 'LaTeX-mode-hook 'LaTeX-math-mode)

;; Reftex mode
; https://tex.stackexchange.com/questions/36876/reftex-doesnt-turn-on-automatically-when-loading-auctex-after-upgrade-to-tex-li
(add-hook 'LaTeX-mode-hook 'turn-on-reftex)
(setq reftex-plug-into-AUCTeX t)

;;;;;;; FUNCTIONS ;;;;;;;
;; Open big files easier
; https://stackoverflow.com/questions/18316665/how-to-improve-emacs-performance-when-view-large-file
(defun my-find-file-check-make-large-file-read-only-hook ()
  "If a file is over a given size, make the buffer read only."
  (when (> (buffer-size) (* 1024 1024))
    (setq buffer-read-only t)
    (buffer-disable-undo)
    (fundamental-mode)))

(add-hook 'find-file-hook 'my-find-file-check-make-large-file-read-only-hook)

;;;;;;;;;;;;;;;;;;;;; PACKAGES ;;;;;;;;;;;;;;;;;;;;;;;
;; Added by Package.el.
(package-initialize)

;; Melpa
(require 'package)
(add-to-list 'package-archives ' ("melpa-stable" . "https://stable.melpa.org/packages/"))

;;;;;;; BASIC ;;;;;;;
;; Dismiss startup
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(LaTeX-math-abbrev-prefix "¬")
 '(inhibit-startup-screen t)
 '(ispell-highlight-face (quote flyspell-incorrect))
 '(package-selected-packages (quote (haskell-mode auctex))))

;; ;; Custom theme
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:inherit nil :stipple nil :background "black" :foreground "white" :inverse-video nil :box nil :strike-through nil :overline nil :underline nil :slant normal :weight normal :height 107 :width normal :foundry "PfEd" :family "DejaVu Sans Mono"))))
 '(cursor ((t (:background "lime green"))))
 '(custom-button ((t (:background "dark slate gray" :foreground "white" :box (:line-width 2 :style released-button)))))
 '(custom-button-mouse ((t (:background "slate gray" :foreground "white" :box (:line-width 2 :style released-button)))))
 '(custom-button-pressed ((t (:background "dark slate gray" :foreground "white" :box (:line-width 2 :style pressed-button)))))
 '(font-lock-comment-delimiter-face ((t (:inherit font-lock-comment-face))))
 '(font-lock-comment-face ((t (:foreground "dark gray"))))
 '(font-lock-doc-face ((t (:inherit (font-lock-comment-face bold)))))
 '(font-lock-function-name-face ((t (:foreground "lime green"))))
 '(font-lock-keyword-face ((t (:foreground "deep pink"))))
 '(font-lock-string-face ((t (:foreground "light goldenrod"))))
 '(font-lock-type-face ((t (:inherit bold :foreground "deep sky blue"))))
 '(haskell-interactive-face-garbage ((t (:inherit font-lock-doc-face))))
 '(haskell-interactive-face-result ((t (:inherit font-lock-doc-face))))
 '(haskell-literate-comment-face ((t (:inherit font-lock-comment-face))))
 '(haskell-quasi-quote-face ((t (:inherit font-lock-doc-face))))
 '(line-number-current-line ((t (:inherit line-number :background "black" :foreground "blue"))))
 '(link ((t (:foreground "magenta" :underline t))))
 '(mode-line ((t (:background "dark slate gray" :foreground "white" :box (:line-width -1 :style released-button)))))
 '(preview-reference-face ((t nil))))
