;;;;;;;;;;;;;;;;;;;;; PACKAGES ;;;;;;;;;;;;;;;;;;;;;;;
;; Added by Package.el.
(package-initialize)

;; Melpa
(require 'package)
(add-to-list 'package-archives ' ("melpa-stable" . "https://stable.melpa.org/packages/"))

;;;;;;;;;;;;;;;;;;;;; MODES ;;;;;;;;;;;;;;;;;;;;;;;
;; Agda mode
(load-file (let ((coding-system-for-read 'utf-8))
	     (shell-command-to-string "agda-mode locate")))

;; Spell check
(add-hook 'text-mode-hook 'flyspell-mode)
(add-hook 'prog-mode-hook 'flyspell-prog-mode)

;;;;;;;;;;;;;;;;;;;;; EDITOR ;;;;;;;;;;;;;;;;;;;;;;;
;; Trailing Whitespace
(setq-default show-trailing-whitespace t)

;; Line Number
(global-linum-mode 1)

;; Column number
(setq column-number-mode t)

;; Dismiss startup
(custom-set-variables
 '(inhibit-startup-screen t)
 '(package-selected-packages (quote (haskell-mode auctex))))
(custom-set-faces)

;; Open big files easier
; https://stackoverflow.com/questions/18316665/how-to-improve-emacs-performance-when-view-large-file
(defun my-find-file-check-make-large-file-read-only-hook ()
  "If a file is over a given size, make the buffer read only."
  (when (> (buffer-size) (* 1024 1024))
    (setq buffer-read-only t)
    (buffer-disable-undo)
    (fundamental-mode)))

(add-hook 'find-file-hook 'my-find-file-check-make-large-file-read-only-hook)
