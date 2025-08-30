type Variant = "primary" | "secondary" | "outline"

interface btnProps {
    variant: Variant
    className?: string
    name?: string
    onClick?: () => void
}

function variantStyle(variant: Variant) {
    if (variant == "primary") {
        return "bg-blue-800 min-h-5 min-w-5 text-white p-1 rounded hover:bg-blue-600 ml-2 px-6 py-2"
    }
    if (variant == "secondary") {
        return "bg-red-800 min-h-5 min-w-5 text-white p-1 rounded hover:bg-red-600 ml-2 px-6 py-2"
    }
    if (variant == "outline") {
        return "outline min-h-5 min-w-5 text-white p-1 rounded hover:bg-white hover:text-black ml-2 px-6 py-2"
    }
}

export default function Button (props: btnProps) {
    return (
        <button 
            className={variantStyle(props.variant) + "" + props.className}
            onClick={props.onClick}
        >
            {props.name}
        </button>
    )
}