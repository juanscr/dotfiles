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
(global-linum-mode 1)

;; Column number
(setq column-number-mode t)

;; Hide tool bar
; https://superuser.com/questions/127420/how-can-i-hide-the-tool-bar-in-emacs-persistently
(tool-bar-mode -1)

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

;;;;;;; BASIC ;;;;;;;
;; Dismiss startup
(custom-set-variables
 '(inhibit-startup-screen t)
 '(package-selected-packages (quote (haskell-mode auctex))))
(custom-set-faces)


;;;;;;;;;;;;;;;;;;;;; PACKAGES ;;;;;;;;;;;;;;;;;;;;;;;
;; Added by Package.el.
(package-initialize)

;; Melpa
(require 'package)
(add-to-list 'package-archives ' ("melpa-stable" . "https://stable.melpa.org/packages/"))
