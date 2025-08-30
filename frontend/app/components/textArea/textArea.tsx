interface textAreaProps {
    placeholder: string,
    value: string,
    onChange?: (e: any) => void
}

export default function TextArea(props: textAreaProps) {
    return (
        <textarea
            className={"outline-none rounded-2xl min-w-5 text-white w-full h-20 bg-transparent p-3 resize-none leading-[3rem]"}
            value={props.value}
            placeholder={props.placeholder}
            onChange={props.onChange}
        />
    )
}