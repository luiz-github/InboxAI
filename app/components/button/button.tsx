type Variant = "primary" | "secondary"

interface btnProps {
    variant: Variant
    name?: string
    onClick?: () => void
}

function variantStyle(variant: Variant) {
    if (variant == "primary") {
        return "bg-blue-800 min-h-5 min-w-5 text-white p-1 rounded"
    }
    if (variant == "secondary") {
        return "bg-red-800 min-h-5 min-w-5 text-white p-1 rounded"
    }
}

export default function Button (props: btnProps) {
    return (
        <button 
            className={variantStyle(props.variant)}
            onClick={props.onClick}
        >
            {props.name}
        </button>
    )
}