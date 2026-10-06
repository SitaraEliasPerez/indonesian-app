import { render, screen, fireEvent } from "@testing-library/react";
import Flashcard from "./Flashcard";

const mockWord = { indonesian: "halo", english: "hello" };
const noop = () => {};

test("shows Indonesian word on front", () => {
  render(<Flashcard word={mockWord} onNext={noop} onPrev={noop} />);
  expect(screen.getByText("halo")).toBeInTheDocument();
});

test("shows English word after flip", () => {
  render(<Flashcard word={mockWord} onNext={noop} onPrev={noop} />);
  fireEvent.click(screen.getByText("halo"));
  expect(screen.getByText("hello")).toBeInTheDocument();
});

test("calls onNext when Next is clicked", () => {
  const onNext = vi.fn();
  render(<Flashcard word={mockWord} onNext={onNext} onPrev={noop} />);
  fireEvent.click(screen.getByText("Next →"));
  expect(onNext).toHaveBeenCalledTimes(1);
});

test("calls onPrev when Prev is clicked", () => {
  const onPrev = vi.fn();
  render(<Flashcard word={mockWord} onNext={noop} onPrev={onPrev} />);
  fireEvent.click(screen.getByText("← Prev"));
  expect(onPrev).toHaveBeenCalledTimes(1);
});