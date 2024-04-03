from django.conf import settings

CONFIG_DEFAULTS = {
    "SITE_TITLE": None,
    "SITE_HEADER": None,
    "SITE_URL": "/",
    "SITE_ICON": None,
    "SITE_SYMBOL": None,
    "SITE_LOGO": None,
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "COLORS": {
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
    "DASHBOARD_CALLBACK": None,
    "ENVIRONMENT": None,
    "STYLES": [],
    "SCRIPTS": [],
    "SIDEBAR": {
        "show_search": False,
        "show_all_applications": False,
        "navigation": {},
    },
    "TABS": [],
    "LOGIN": {
        "image": None,
        "redirect_after": None,
    },
    "EXTENSIONS": {"modeltranslation": {"flags": {}}},
}

LABEL_CLASSES = [
    "block",
    "font-medium",
    "mb-2",
    "text-gray-900",
    "text-sm",
    "dark:text-gray-200",
]

CHECKBOX_LABEL_CLASSES = [
    "ml-2",
    "text-sm",
    "text-gray-900",
    "dark:text-gray-200",
]

BASE_CLASSES = [
    "border",
    "bg-white",
    "font-medium",
    "rounded-md",
    "shadow-sm",
    "text-gray-500",
    "text-sm",
    "focus:ring",
    "focus:ring-primary-300",
    "focus:border-primary-600",
    "focus:outline-none",
    "group-[.errors]:border-red-600",
    "group-[.errors]:focus:ring-red-200",
    "dark:bg-gray-900",
    "dark:border-gray-700",
    "dark:text-gray-400",
    "dark:focus:border-primary-600",
    "dark:focus:ring-primary-700",
    "dark:focus:ring-opacity-50",
    "dark:group-[.errors]:border-red-500",
    "dark:group-[.errors]:focus:ring-red-600/40",
]

BASE_INPUT_CLASSES = [
    *BASE_CLASSES,
    "px-3",
    "py-2",
    "w-full",
]

INPUT_CLASSES = [*BASE_INPUT_CLASSES, "max-w-2xl"]

COLOR_CLASSES = [*BASE_CLASSES, "h-9.5", "px-2", "py-2", "w-32"]

INPUT_CLASSES_READONLY = [*BASE_INPUT_CLASSES, "bg-gray-50"]

TEXTAREA_CLASSES = [
    *BASE_INPUT_CLASSES,
    "max-w-4xl",
    "appearance-none",
    "expandable",
    "overflow-hidden",
    "transition",
    "transition-height",
    "duration-75",
    "ease-in-out",
    "resize-none",
]

TEXTAREA_EXPANDABLE_CLASSES = [
    "absolute",
    "bottom-0",
    "left-0",
    "right-0",
    "top-0",
    "h-full",
]

SELECT_CLASSES = [
    *BASE_INPUT_CLASSES,
    "pr-8",
    "max-w-2xl",
    "appearance-none",
    "truncate",
]

PROSE_CLASSES = [
    "font-normal",
    "prose-sm",
    "prose-blockquote:border-l-4",
    "prose-blockquote:not-italic",
    "prose-pre:bg-gray-50",
    "prose-pre:rounded",
    "prose-headings:font-medium",
    "prose-a:text-primary-600",
    "prose-a:underline",
    "prose-headings:font-medium",
    "prose-headings:text-gray-700",
    "prose-ol:list-decimal",
    "prose-ul:list-disc",
    "prose-strong:text-gray-700",
    "dark:prose-pre:bg-gray-800",
    "dark:prose-blockquote:border-gray-700",
    "dark:prose-blockquote:text-gray-400",
    "dark:prose-headings:text-gray-200",
    "dark:prose-strong:text-gray-200",
]

CHECKBOX_CLASSES = [
    "appearance-none",
    "bg-white",
    "block",
    "border",
    "border-gray-300",
    "cursor-pointer",
    "h-4",
    "relative",
    "rounded",
    "shadow-sm",
    "w-4",
    "hover:border-gray-400",
    "dark:bg-gray-700",
    "dark:border-gray-500",
    "dark:after:checked:text-white",
    "focus:outline",
    "focus:outline-1",
    "focus:outline-offset-2",
    "focus:outline-primary-500",
    "after:absolute",
    "after:content-['done']",
    "after:!flex",
    "after:h-4",
    "after:items-center",
    "after:justify-center",
    "after:leading-none",
    "after:material-symbols-outlined",
    "after:-ml-px",
    "after:-mt-px",
    "after:!text-sm",
    "after:text-white",
    "after:transition-all",
    "after:w-4",
    "after:dark:text-gray-700",
    "checked:bg-primary-600",
    "checked:border-primary-600",
    "checked:transition-all",
    "checked:hover:border-primary-600",
]

RADIO_CLASSES = [
    "appearance-none",
    "bg-white",
    "block",
    "border",
    "border-gray-300",
    "cursor-pointer",
    "h-4",
    "relative",
    "rounded-full",
    "w-4",
    "dark:bg-gray-700",
    "dark:border-gray-500",
    "hover:border-gray-400",
    "focus:outline",
    "focus:outline-1",
    "focus:outline-offset-2",
    "focus:outline-primary-500",
    "after:absolute",
    "after:bg-white",
    "after:content-['']",
    "after:flex",
    "after:h-2",
    "after:items-center",
    "after:justify-center",
    "after:leading-none",
    "after:left-1/2",
    "after:rounded-full",
    "after:text-white",
    "after:top-1/2",
    "after:transition-all",
    "after:-translate-x-1/2",
    "after:-translate-y-1/2",
    "after:text-sm",
    "after:w-2",
    "after:dark:text-gray-700",
    "after:dark:bg-transparent",
    "checked:bg-primary-600",
    "checked:border-primary-600",
    "checked:transition-all",
    "checked:after:bg-white",
    "checked:after:dark:bg-gray-200",
]

SWITCH_CLASSES = [
    "appearance-none",
    "bg-gray-300",
    "cursor-pointer",
    "h-5",
    "relative",
    "rounded-full",
    "transition-all",
    "w-8",
    "after:absolute",
    "after:bg-white",
    "after:content-['']",
    "after:bg-red-300",
    "after:h-3",
    "after:rounded-full",
    "after:shadow-sm",
    "after:left-1",
    "after:top-1",
    "after:w-3",
    "checked:bg-primary-600",
    "checked:after:left-4",
    "dark:bg-gray-600",
]



def get_config(settings_name=None):
    if settings_name is None:
        settings_name = "UNFOLD"
        
    return {
        **CONFIG_DEFAULTS,
        "LABEL_CLASSES": LABEL_CLASSES,
        "CHECKBOX_LABEL_CLASSES": CHECKBOX_LABEL_CLASSES,
        "BASE_CLASSES": BASE_CLASSES,
        "BASE_INPUT_CLASSES": BASE_INPUT_CLASSES,
        "INPUT_CLASSES": INPUT_CLASSES,
        "COLOR_CLASSES": COLOR_CLASSES,
        "INPUT_CLASSES_READONLY": INPUT_CLASSES_READONLY,
        "TEXTAREA_CLASSES": TEXTAREA_CLASSES,
        "TEXTAREA_EXPANDABLE_CLASSES": TEXTAREA_EXPANDABLE_CLASSES,
        "SELECT_CLASSES": SELECT_CLASSES,
        "PROSE_CLASSES": PROSE_CLASSES,
        "CHECKBOX_CLASSES": CHECKBOX_CLASSES,
        "RADIO_CLASSES": RADIO_CLASSES,
        "SWITCH_CLASSES": SWITCH_CLASSES,
         **getattr(settings, settings_name, {})
    }
     
