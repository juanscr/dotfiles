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

;;;;;;;;;;;;;;;;;;;;; EDITOR ;;;;;;;;;;;;;;;;;;;;;;;
;; Trailing Whitespace
(setq-default show-trailing-whitespace t)

;; Line Number
(global-linum-mode 1)

;; Column number
(setq column-number-mode t)

;; Spell check
(add-hook 'text-mode-hook 'flyspell-mode)
(add-hook 'prog-mode-hook 'flyspell-prog-mode)

;; Dismiss startup
(custom-set-variables
 '(inhibit-startup-screen t)
 '(package-selected-packages (quote (ein haskell-mode auctex))))
(custom-set-faces)
