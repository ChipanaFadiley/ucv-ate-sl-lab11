from src.main import compare_algorithms, main, run_examples, show_tic_tac_toe_demo


def test_compare_algorithms_prints_both_search_reports(capsys):
    compare_algorithms("Tiny", lambda: [[1, 4], [2, 3]])

    output = capsys.readouterr().out

    assert "Tree: Tiny" in output
    assert "Minimax score:" in output
    assert "Alpha-Beta cuts:" in output


def test_show_tic_tac_toe_demo_prints_agent_choice(capsys):
    show_tic_tac_toe_demo()

    output = capsys.readouterr().out

    assert "Tic-Tac-Toe Alpha-Beta demo" in output
    assert "Agent move:" in output


def test_main_runs_all_examples(capsys):
    run_examples()

    output = capsys.readouterr().out

    assert "Sample Tree" in output
    assert "Medium Tree" in output
    assert "Ordered Tree" in output
    assert "Unbalanced Tree" in output
    assert "Tic-Tac-Toe Alpha-Beta demo" in output


def test_main_without_arguments_runs_examples(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["main.py"])

    main()

    output = capsys.readouterr().out

    assert "Sample Tree" in output
